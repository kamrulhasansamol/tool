@echo off
title XENO OTP - Auto Updater
color 0A

echo ===================================================
echo           XENO OTP - AUTO UPDATER
echo ===================================================
echo.
echo Checking for updates and downloading the latest version...
echo.

:: Replace the URL below with the direct link to your latest executable on GitHub.
:: For example: https://github.com/YOUR_USERNAME/YOUR_REPO/raw/main/XENO_OTP.exe
set "DOWNLOAD_URL=https://github.com/kamrulhasansamol/tool/raw/main/XENO_OTP.exe"

curl -L -o XENO_OTP_new.exe "%DOWNLOAD_URL%"

if exist XENO_OTP_new.exe (
    echo.
    echo [OK] Update downloaded successfully!
    echo Swapping files...
    
    :: Kill the running app if it's open so we can delete it
    taskkill /F /IM "XENO_OTP.exe" >nul 2>&1
    timeout /t 1 /nobreak >nul
    
    :: Delete old file and rename the new one
    if exist XENO_OTP.exe del /F /Q XENO_OTP.exe
    ren XENO_OTP_new.exe XENO_OTP.exe
    
    echo.
    echo [OK] Update Complete! Starting the latest version...
    start XENO_OTP.exe
) else (
    echo.
    echo [ERROR] Failed to download the update. Please check your internet connection or the URL.
    pause
)

:: Exit the updater
exit
