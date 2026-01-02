@echo off
chcp 65001 >nul
:: 上面這行是為了防止中文亂碼

echo ==========================================
echo       正在為您打包程式 (Python -> EXE)
echo ==========================================

:: ▼▼▼ 關鍵修改在這裡 ▼▼▼
echo [步驟 0] 正在啟動虛擬環境...
call venv\Scripts\activate.bat
:: ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲

:: 1. 清理舊檔案 (避免 Icon 卡住或舊程式殘留)
echo [步驟 1/2] 清理舊的 build 與 dist 資料夾...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist main.spec del main.spec

:: 2. 執行 PyInstaller 指令
echo.
echo [步驟 2/2] 開始執行 PyInstaller...
pyinstaller --noconfirm --onefile --windowed --clean --collect-all customtkinter --add-data "assets/doggy_16X16.ico;assets" --icon="assets/doggy_16X16.ico" main.py
echo.
echo ==========================================
if exist "dist\main.exe" (
    echo    恭喜！打包成功！
    echo    檔案位置： dist\main.exe
) else (
    echo    糟糕，打包似乎失敗了...請檢查上面的錯誤訊息。
)
echo ==========================================
pause