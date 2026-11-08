# Locate content autopilot - runner.
# Task Scheduler starts this. setup.ps1 copies it to %LOCALAPPDATA%\LocateAutopilot so it
# still runs if Google Drive hasn't mounted G: yet. If you edit this file, run setup.ps1 again.

param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('plan', 'build')]
    [string]$Job
)

$ErrorActionPreference = 'Continue'
$AppDir  = Split-Path -Parent $MyInvocation.MyCommand.Path
$LogDir  = Join-Path $AppDir 'logs'
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$Stamp   = Get-Date -Format 'yyyy-MM-dd_HHmm'
$Log     = Join-Path $LogDir "$Job-$Stamp.log"
$Summary = Join-Path $LogDir "$Job-summary.txt"
$Config  = Get-Content -LiteralPath (Join-Path $AppDir 'config.json') -Raw | ConvertFrom-Json

function Write-Log([string]$Text) {
    Add-Content -LiteralPath $Log -Encoding UTF8 -Value ("[{0}] {1}" -f (Get-Date -Format 'HH:mm:ss'), $Text)
}

function Send-Ping([string]$Title, [string]$Body, [bool]$Morning) {
    if (-not $Config.ntfyTopic) { return }
    $headers = @{ Title = $Title }
    if ($Morning) {
        $now = Get-Date
        $at  = $now.Date.AddHours([int]$Config.morningHour)
        if ($at -le $now.AddMinutes(1)) { $at = $at.AddDays(1) }
        $headers['At'] = [string]([DateTimeOffset]$at).ToUnixTimeSeconds()
    }
    try {
        $bytes = [Text.Encoding]::UTF8.GetBytes($Body)
        Invoke-RestMethod -Method Post -Uri ("https://ntfy.sh/" + $Config.ntfyTopic) -Body $bytes -Headers $headers -ContentType 'text/plain; charset=utf-8' | Out-Null
        Write-Log "Ping sent: $Title"
    } catch {
        Write-Log "Ping failed: $_"
    }
}

# Keep the PC awake until this script ends (ES_CONTINUOUS | ES_SYSTEM_REQUIRED).
try {
    Add-Type -Namespace LocateAP -Name Power -MemberDefinition '[DllImport("kernel32.dll")] public static extern uint SetThreadExecutionState(uint esFlags);'
    [void][LocateAP.Power]::SetThreadExecutionState([uint32]2147483649)
} catch {
    Write-Log "Could not set keep-awake: $_"
}

$isBuild = ($Job -eq 'build')
Write-Log "Starting $Job job."

# Wait up to 10 minutes for Google Drive to mount after a wake from sleep.
$deadline = (Get-Date).AddMinutes(10)
while (-not (Test-Path -LiteralPath $Config.workspace) -and (Get-Date) -lt $deadline) {
    Start-Sleep -Seconds 20
}
if (-not (Test-Path -LiteralPath $Config.workspace)) {
    Write-Log "Workspace not found: $($Config.workspace)"
    Send-Ping "Content $Job did not run" "Google Drive (G:) wasn't available, so the $Job job didn't run. It will try again at the next scheduled time." $isBuild
    exit 1
}

Remove-Item -LiteralPath $Summary -ErrorAction SilentlyContinue
Set-Location -LiteralPath $Config.workspace

$Scratch = Join-Path $AppDir 'scratch'
New-Item -ItemType Directory -Force -Path $Scratch | Out-Null

$today  = Get-Date -Format 'dddd yyyy-MM-dd'
$prompt = "Today is $today. Follow the instructions in _brand/Content/autopilot/$Job-week.md exactly. This is an unattended scheduled run, so nobody can answer questions: make sensible choices and record them as the instructions say. Your scratch folder on C: is $Scratch . Write the phone summary to this file: $Summary"

# Unattended runs get a fixed tool list, not blanket permissions. Anything not listed
# (deleting files, git, other programs) is refused and the run reports it instead.
$allowed = @(
    'Read', 'Write', 'Edit', 'Glob', 'Grep', 'Skill', 'TodoWrite', 'WebSearch', 'WebFetch',
    'Bash(ls:*)', 'Bash(mkdir:*)', 'Bash(cp:*)', 'Bash(mv:*)', 'Bash(robocopy:*)',
    'Bash(ffmpeg:*)', 'Bash(ffprobe:*)', 'Bash(python:*)', 'Bash(py:*)', 'Bash(whisper:*)',
    'Bash(node:*)', 'Bash(npm install:*)', 'Bash(npm run:*)', 'Bash(npx remotion:*)',
    'Bash(powershell -NoProfile -Command Get-ChildItem:*)'
)
$denied = @('Bash(rm:*)', 'Bash(del:*)', 'Bash(git:*)', 'Bash(curl:*)')

Write-Log "Running Claude Code."
& $Config.claude -p $prompt --permission-mode acceptEdits --add-dir $Scratch --allowedTools $allowed --disallowedTools $denied 2>&1 | Out-File -LiteralPath $Log -Append -Encoding utf8
$code = $LASTEXITCODE
Write-Log "Claude Code finished with exit code $code."

$text = ''
if (Test-Path -LiteralPath $Summary) { $text = (Get-Content -LiteralPath $Summary -Raw).Trim() }

if ($code -ne 0 -or -not $text) {
    Send-Ping "Content $Job had a problem" "The $Job run stopped early (exit code $code). Log on your PC: $Log" $isBuild
} elseif ($text -ne 'NOTHING') {
    if ($isBuild) { $title = 'Content ready to review' } else { $title = 'Your content week is planned' }
    Send-Ping $title $text $isBuild
} else {
    Write-Log 'Nothing to report.'
}

# Tidy render scratch older than 3 days (only inside the autopilot's own scratch folder).
Get-ChildItem -LiteralPath $Scratch -Force |
    Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-3) } |
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

# Tidy logs older than 30 days.
Get-ChildItem -LiteralPath $LogDir -Filter '*.log' -File |
    Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) } |
    Remove-Item -ErrorAction SilentlyContinue

exit $code
