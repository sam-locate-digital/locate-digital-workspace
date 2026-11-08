# Locate content autopilot - one-time setup.
# Right-click this file and choose "Run with PowerShell". Safe to run again at any time.
# It sets up two scheduled jobs on this PC:
#   Locate - Weekly content plan   Sundays 6:00pm
#   Locate - Nightly content build every night 10:00pm

$ErrorActionPreference = 'Stop'

function Say([string]$Text, [string]$Colour = 'White') { Write-Host $Text -ForegroundColor $Colour }

try {
    $Here      = Split-Path -Parent $MyInvocation.MyCommand.Path
    $Workspace = (Resolve-Path (Join-Path $Here '..\..\..')).Path
    $AppDir    = Join-Path $env:LOCALAPPDATA 'LocateAutopilot'
    $CfgPath   = Join-Path $AppDir 'config.json'

    Say ''
    Say 'Locate content autopilot setup' 'Cyan'
    Say "Workspace: $Workspace"

    if (-not (Test-Path -LiteralPath (Join-Path $Workspace '_brand\Content\CLAUDE.md'))) {
        throw "This doesn't look like the Locate workspace. Keep setup.ps1 in _brand\Content\autopilot and run it from there."
    }

    # 1. Find Claude Code.
    Say ''
    Say '1. Finding Claude Code...'
    $candidates = @(
        (Join-Path $env:USERPROFILE '.local\bin\claude.exe'),
        (Get-Command claude.exe -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source -First 1),
        (Get-Command claude.cmd -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source -First 1),
        (Get-Command claude -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source -First 1)
    ) | Where-Object { $_ -and (Test-Path -LiteralPath $_) }
    $Claude = $candidates | Select-Object -First 1
    if (-not $Claude) { throw "Couldn't find Claude Code. Open a terminal, run 'claude' once to check it works, then run this setup again." }
    Say "   Found: $Claude" 'Green'

    Say '   Checking it can run on its own (takes a few seconds)...'
    Push-Location -LiteralPath $Workspace
    $ErrorActionPreference = 'Continue'
    $test = (& $Claude -p 'Reply with only the word READY' 2>&1 | Out-String)
    $ErrorActionPreference = 'Stop'
    Pop-Location
    if ($test -notmatch 'READY') {
        Say '   Claude Code did not answer as expected. Its reply was:' 'Yellow'
        Say $test 'Yellow'
        throw "Open a terminal, run 'claude' and sign in if asked, then run this setup again."
    }
    Say '   Claude Code works unattended.' 'Green'

    # 2. Config and runner on C: (so the jobs start even before Google Drive mounts).
    Say ''
    Say '2. Saving settings...'
    New-Item -ItemType Directory -Force -Path $AppDir | Out-Null
    $topic = $null
    if (Test-Path -LiteralPath $CfgPath) {
        try { $topic = (Get-Content -LiteralPath $CfgPath -Raw | ConvertFrom-Json).ntfyTopic } catch { $topic = $null }
    }
    if (-not $topic) { $topic = 'locate-sam-' + ([guid]::NewGuid().ToString('N').Substring(0, 12)) }
    $cfg = [ordered]@{
        workspace   = $Workspace
        claude      = $Claude
        ntfyTopic   = $topic
        morningHour = 7
    }
    $cfg | ConvertTo-Json | Set-Content -LiteralPath $CfgPath -Encoding UTF8
    Copy-Item -LiteralPath (Join-Path $Here 'run.ps1') -Destination (Join-Path $AppDir 'run.ps1') -Force
    Say "   Saved to $AppDir" 'Green'

    # 3. Let scheduled jobs wake the PC from sleep.
    Say ''
    Say '3. Allowing wake timers...'
    powercfg /SETACVALUEINDEX SCHEME_CURRENT SUB_SLEEP RTCWAKE 1 | Out-Null
    $okAc = ($LASTEXITCODE -eq 0)
    powercfg /SETDCVALUEINDEX SCHEME_CURRENT SUB_SLEEP RTCWAKE 1 | Out-Null
    powercfg /SETACTIVE SCHEME_CURRENT | Out-Null
    if ($okAc) { Say '   Done. The PC can wake from sleep for the jobs.' 'Green' }
    else { Say '   Could not change the power setting. The jobs still run whenever the PC is awake.' 'Yellow' }

    # 4. Register the two jobs.
    Say ''
    Say '4. Creating the scheduled jobs...'
    $ps = Join-Path $env:SystemRoot 'System32\WindowsPowerShell\v1.0\powershell.exe'
    $runner = Join-Path $AppDir 'run.ps1'
    $settings = New-ScheduledTaskSettingsSet -WakeToRun -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Hours 4) -MultipleInstances IgnoreNew

    $jobs = @(
        @{ Name = 'Locate - Weekly content plan'; Job = 'plan'; Trigger = (New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At '18:00');
           Desc = 'Plans next week of @locatingsam content, writes scripts and hand-over folders. See _brand\Content\autopilot\README.md' },
        @{ Name = 'Locate - Nightly content build'; Job = 'build'; Trigger = (New-ScheduledTaskTrigger -Daily -At '22:00');
           Desc = 'Edits reels and builds carousels whose files have arrived. See _brand\Content\autopilot\README.md' }
    )
    foreach ($j in $jobs) {
        $arg = "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$runner`" -Job $($j.Job)"
        $action = New-ScheduledTaskAction -Execute $ps -Argument $arg
        Register-ScheduledTask -TaskName $j.Name -Action $action -Trigger $j.Trigger -Settings $settings -Description $j.Desc -Force | Out-Null
        Say "   $($j.Name)" 'Green'
    }

    # 5. Phone notifications.
    Say ''
    Say '5. Phone notifications' 'Cyan'
    Say '   Install the free "ntfy" app (App Store or Google Play), tap +, and subscribe to this topic:'
    Say ''
    Say "      $topic" 'Yellow'
    Say ''
    try { Set-Clipboard -Value $topic; Say '   (It is copied to your clipboard.)' } catch { }
    Say '   Keep the topic name private. Anyone who has it can read your notifications.'
    Read-Host '   Press Enter once you have subscribed, to send a test notification'
    try {
        Invoke-RestMethod -Method Post -Uri "https://ntfy.sh/$topic" -Headers @{ Title = 'Locate autopilot is set up' } -Body 'You will get a ping on Sunday evening with the week plan, and at 7am after a night when something was built.' | Out-Null
        Say '   Test sent. Check your phone.' 'Green'
    } catch {
        Say "   Couldn't send the test: $_" 'Yellow'
    }

    # 6. Optional first run.
    Say ''
    $answer = Read-Host '6. Plan next week right now instead of waiting for Sunday? (y/n)'
    if ($answer -match '^[yY]') {
        Start-ScheduledTask -TaskName 'Locate - Weekly content plan'
        Say '   Started in the background. You will get a ping when the plan is ready (usually 10-20 minutes).' 'Green'
    }

    Say ''
    Say 'All set. To pause or remove the jobs, open Task Scheduler and look for the two "Locate - " tasks.' 'Cyan'
} catch {
    Say ''
    Say "Setup stopped: $($_.Exception.Message)" 'Red'
}

Say ''
Read-Host 'Press Enter to close'
