@echo off
title XENO OTP - Build and Auto-Upload
color 0B

echo ===================================================
echo       XENO OTP - BUILD AND AUTO-UPLOAD TO GITHUB
echo ===================================================
echo.

echo [1/4] Extracting version from main.py and updating version.txt...
:: Automatically extract CURRENT_VERSION from main.py and write it to version.txt
python -c "import re; c=open('main.py', encoding='utf-8').read(); m=re.search(r'CURRENT_VERSION\s*=\s*([0-9.]+)', c); url='https://github.com/kamrulhasansamol/tool/raw/main/XENO_OTP.exe'; open('version.txt','w', encoding='utf-8').write(f'{m.group(1)}\n{url}') if m else print('Version not found in main.py')"

echo.
echo [2/4] Building executable...
pyinstaller --onefile --console --name "XENO_OTP" --clean main.py

if exist "dist\XENO_OTP.exe" (
    echo.
    echo [3/4] Moving executable to main folder...
    copy /Y "dist\XENO_OTP.exe" "XENO_OTP.exe" >nul
    
    echo.
    echo [4/4] Uploading to GitHub...
    git add XENO_OTP.exe
    git add main.py
    git add version.txt
    
    :: Use current date and time as commit message
    for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
    set commit_msg=Auto Update %datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2%
    
    git commit -m "%commit_msg%"
    git push origin main
    
    echo.
    echo ===================================================
    echo [SUCCESS] Build and Upload complete!
    echo Your users can now auto-update to this version.
    echo ===================================================
) else (
    echo.
    echo [ERROR] Build failed! Cannot upload.
)

pause
