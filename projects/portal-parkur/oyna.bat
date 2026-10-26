@echo off
rem Portal Parkur - oyunu Godot 4.7.2 ile baslatir (ilk acilis birkac saniye shader derler)
set GODOT=C:\tools\godot\Godot_v4.7.2-stable_win64.exe
if not exist "%GODOT%" (
  echo Godot bulunamadi: %GODOT%
  echo https://github.com/godotengine/godot/releases/tag/4.7.2-stable adresinden Godot_v4.7.2-stable_win64.exe.zip indirip C:\tools\godot icine acin.
  pause
  exit /b 1
)
"%GODOT%" --path "%~dp0" --resolution 1600x900
