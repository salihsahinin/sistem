# JARVIS gece-senkron (deneysel m.29; karar 2026-07-19: Model A + C asisi — senaryo-defteri blogu)
# Ne yapar: her gece origin->PC ff-only esitleme + log satiri; basarisizlikta HICBIR SEYE DOKUNMAZ, sabaha uyari birakir.
# Kayit (Salih, tek sefer, Windows terminali):
#   schtasks /Create /TN "JARVIS-gece-senkron" /TR "powershell -ExecutionPolicy Bypass -File C:\JARVIS\tools\gece-senkron.ps1" /SC DAILY /ST 06:00
$repo = "C:\JARVIS"
$log  = Join-Path $repo "raporlar\usage\senkron-log.jsonl"
Set-Location $repo
$t0 = Get-Date
git fetch origin 2>&1 | Out-Null
$before = (git rev-parse HEAD).Trim()
git pull --ff-only origin main 2>&1 | Out-Null
$ok = ($LASTEXITCODE -eq 0)
$after = (git rev-parse HEAD).Trim()
$dirty = (git status --porcelain | Measure-Object -Line).Lines
$dur = [int]((Get-Date) - $t0).TotalSeconds
$status = if ($ok) { "OK" } else { "FAIL-ff" }
$line = '{"ts":"' + (Get-Date -Format o) + '","event":"gece-senkron","status":"' + $status + '","from":"' + $before.Substring(0,7) + '","to":"' + $after.Substring(0,7) + '","dirty_files":' + $dirty + ',"dur_s":' + $dur + ',"agent":"script","model":"none","tokens":0}'
Add-Content -Path $log -Value $line
if (-not $ok) {
  $uyari = Join-Path $repo "raporlar\usage\SENKRON-UYARI.md"
  Add-Content -Path $uyari -Value ("FAIL " + (Get-Date -Format o) + " - ff-only ilerleyemedi (yerel degisiklik/dal sapmasi). C-asisi geregi DOKUNULMADI; elle bak: git status + git pull --ff-only")
}
