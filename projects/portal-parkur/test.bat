@echo off
rem Otomatik mekanik testi: sanal girdiyle kosar, test_cikti\ icine ekran goruntusu + rapor.json yazar
set PP_TEST=1
"C:\tools\godot\Godot_v4.7.2-stable_win64_console.exe" --path "%~dp0" --resolution 1600x900
echo cikis kodu (basarisiz test sayisi): %ERRORLEVEL%
