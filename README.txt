===========================================================
               水利工程分析工具 (Project 1229)
===========================================================

[ 快速指令 ]
1. 啟動程式：  python main.py
2. 打包 EXE：  點擊 build.bat
3. 安裝套件：  pip install -r requirements.txt

-----------------------------------------------------------
[ 檔案結構說明 ]

1. 根目錄 (核心入口)
   ├─ main.py            : 程式的啟動入口 (只負責啟動 App)。
   ├─ config.json        : 使用者設定檔 (視窗大小、預設參數)，打包後需複製到 EXE 旁邊。
   ├─ build.bat          : 自動打包成 EXE 的腳本。
   └─ requirements.txt   : 紀錄專案用到的所有套件清單。

2. core/ (大腦：純邏輯與工具)
   ├─ utility.py         : 路徑工具 (負責在 EXE 中找到圖片正確位置)。
   ├─ configLoader.py    : 負責讀取 config.json，含防呆機制。
   ├─ logger.py          : 錯誤紀錄系統 (產生 log 檔)。
   └─ logic/             : 數學運算核心
      ├─ sample_test.py  : 水文公式計算 (Q=CIA)。
      └─ fileLoader.py   : Excel/CSV 檔案讀取邏輯。

3. gui/ (臉面：視窗介面)
   ├─ app.py             : 主視窗程式 (負責組裝各個分頁)。
   ├─ plot_utils.py      : 繪圖工具 (設定 Matplotlib 中文字體、畫布)。
   └─ tabs/              : 功能分頁
      ├─ hydro_tab.py    : [分頁1] 水文計算器。
      ├─ file_tab.py     : [分頁2] 檔案讀取器。
      └─ channel_tab.py  : [分頁3] 河道斷面繪圖 (HEC-RAS 模擬)。

4. 其他資料夾
   ├─ assets/            : 存放圖片、Icon (.ico)。
   ├─ venv/              : Python 虛擬環境 (絕對不要動)。
   └─ dist/              : 打包完成的 EXE 會出現在這裡。

-----------------------------------------------------------
[ 注意事項 ]
* 若要修改預設參數，請直接編輯 config.json。
* 若圖表中文顯示亂碼，請檢查 gui/plot_utils.py 中的字體設定。