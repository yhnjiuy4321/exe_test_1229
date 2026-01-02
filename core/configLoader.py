import json
import os
import sys

# 預設設定 (萬一找不到檔案時的備案)
DEFAULT_CONFIG = {
    "window": {
        "width": 800,
        "height": 600,
        "theme": "blue"
    },
    "defaults": {
        "b": 10,
        "z": 2,
        "n": 0.025
    }
}


def get_config_path():
    """
    取得 config.json 的絕對路徑
    邏輯：永遠只找「執行檔 (EXE) 或 入口腳本 (main.py)」旁邊的那一個
    """
    if getattr(sys, 'frozen', False):
        # 如果是打包後的 EXE，基準點是 EXE 所在的資料夾
        base_path = os.path.dirname(sys.executable)
    else:
        # 如果是開發模式 (main.py)，基準點是專案根目錄
        base_path = os.path.abspath(".")

    return os.path.join(base_path, "config.json")


def load_config():
    """ 讀取設定檔，讀失敗就回傳預設值 """
    path = get_config_path()

    if not os.path.exists(path):
        print(f"⚠️ 找不到設定檔：{path}，將使用內建預設值。")
        return DEFAULT_CONFIG

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"✅ 成功載入設定：{path}")
            return data
    except Exception as e:
        print(f"❌ 設定檔讀取錯誤：{e}，將使用預設值。")
        return DEFAULT_CONFIG