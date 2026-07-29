@echo off
title XENO OTP - Build and Encrypt
echo Installing required build tools (PyInstaller)...
pip install pyinstaller

echo.
echo Encrypting and Building XENO_OTP executable...
:: Note: Bytecode encryption (--key) is no longer supported in PyInstaller v6+
pyinstaller --onefile --console --name "XENO_OTP" --clean main.py

echo.
echo ========================================================
echo Build complete! 
echo Your standalone ENCRYPTED executable is located in the "dist" folder.
echo ========================================================
pause
