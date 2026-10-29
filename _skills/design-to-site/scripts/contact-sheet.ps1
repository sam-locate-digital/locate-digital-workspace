<#
  Contact sheet of images, each labelled with its index, file name and size. Use it to match loose
  photos to the canvas photo list, or to review a folder of QA screenshots at a glance.

    powershell -File contact-sheet.ps1 -Dir <folder> -Out <sheet.png> [-Filter *.png] [-Cols 4] [-Width 360] [-Crop 0]

  -Crop N keeps only the top N source pixels of each image (handy for tall full-page screenshots).
#>
param(
  [Parameter(Mandatory = $true)][string]$Dir,
  [Parameter(Mandatory = $true)][string]$Out,
  [string]$Filter = '*.png',
  [int]$Cols = 4,
  [int]$Width = 360,
  [int]$Crop = 0
)
Add-Type -AssemblyName System.Drawing
$files = Get-ChildItem $Dir -Filter $Filter | Sort-Object Name
if (-not $files) { Write-Error "No files matching $Filter in $Dir"; exit 1 }

# Cell height from the tallest (cropped) aspect ratio, capped so the sheet stays readable.
$ratio = 0
foreach ($f in $files) { $img = [System.Drawing.Image]::FromFile($f.FullName); $h = if ($Crop -gt 0) { [math]::Min($Crop, $img.Height) } else { $img.Height }; $ratio = [math]::Max($ratio, $h / $img.Width); $img.Dispose() }
$cellH = [int][math]::Min($Width * $ratio, $Width * 8)
$rows = [math]::Ceiling($files.Count / $Cols)
$sheet = New-Object System.Drawing.Bitmap ($Width * $Cols), (($cellH + 20) * $rows)
$g = [System.Drawing.Graphics]::FromImage($sheet); $g.Clear([System.Drawing.Color]::White)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$font = New-Object System.Drawing.Font 'Arial', 9
$i = 0
foreach ($f in $files) {
  $img = [System.Drawing.Image]::FromFile($f.FullName)
  $x = ($i % $Cols) * $Width; $y = [math]::Floor($i / $Cols) * ($cellH + 20)
  $srcH = if ($Crop -gt 0) { [math]::Min($Crop, $img.Height) } else { $img.Height }
  $scale = [math]::Min(($Width - 6) / $img.Width, $cellH / $srcH)
  $dst = New-Object System.Drawing.Rectangle $x, ($y + 18), ([int]($img.Width * $scale)), ([int]($srcH * $scale))
  $src = New-Object System.Drawing.Rectangle 0, 0, $img.Width, $srcH
  $g.DrawImage($img, $dst, $src, [System.Drawing.GraphicsUnit]::Pixel)
  $g.DrawString("$i  $($f.Name)  $($img.Width)x$($img.Height)", $font, [System.Drawing.Brushes]::Black, $x, $y + 2)
  $img.Dispose(); $i++
}
$sheet.Save($Out); $g.Dispose(); $sheet.Dispose()
Write-Output "Saved $Out ($($files.Count) images)"
