call ..\Server_settings\config.bat

@echo off
"%bashDirectory%" "%~dp0\CloudflareDDNS.sh"
EXIT /B

