# Downloads the 12 Higgsfield photos for the Harlow Home Loans demo into .\images
# Run from this folder:  powershell -ExecutionPolicy Bypass -File .\download-images.ps1
# (or right-click > Run with PowerShell)

$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$manifest = Join-Path $here "image-manifest.csv"
$outDir = Join-Path $here "images"

if (-not (Test-Path $manifest)) { throw "image-manifest.csv not found next to this script." }
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$rows = Import-Csv $manifest
$ok = 0
foreach ($row in $rows) {
  $dest = Join-Path $outDir $row.file
  try {
    Invoke-WebRequest -Uri $row.source_url -OutFile $dest -UseBasicParsing
    Write-Host "Saved $($row.file)"
    $ok++
  } catch {
    Write-Warning "Could not download $($row.file): $($_.Exception.Message)"
  }
}

Write-Host ""
Write-Host "$ok of $($rows.Count) photos saved to $outDir"
Read-Host "Press Enter to close"
