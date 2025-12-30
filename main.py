# 檔案位置：main.py (在最外層)

# ▼▼▼ 關鍵連接 3：從 core 資料夾匯入 gui ▼▼▼
from core.gui import start_gui

# ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲

if __name__ == "__main__":
    # 這裡可以做一些環境檢查，或是讀取設定檔
    print("程式啟動中...")

    # 啟動介面
    start_gui()
