# 上傳讀取excel csv檔 給我程式碼
import os
import sys
from tkinter import filedialog

import pandas as pd

#
# # 讀取 Excel 檔案
# df = pd.read_excel('../TEST0102.xlsx')
#
# # 讀取 CSV 檔案
# dfc = pd.read_csv('../TEST0102.csv')
#
# # 顯示前五列數據
# print(df.head())
#
# print(dfc.head())

"""
 獲取資源的絕對路徑，適用於開發環境與 PyInstaller 打包後的應用程式。
 """


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller 打包後的臨時目錄
    except AttributeError:
        base_path = os.path.abspath(".")  # 開發環境中的當前目錄

    full_path = os.path.join(base_path, relative_path)

    # 檢查路徑是否存在
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"資源檔案未找到: {full_path}")

    return full_path


"""
 讀取 CSV 或 Excel 檔案，並回傳資料
 回傳: (資料內容字串, 欄位清單)
 """


def load_data(file_path):
    try:
        # 1. 判斷副檔名
        ext = os.path.splitext(file_path)[-1].lower()

        if ext == '.csv':
            # 讀取 CSV
            df = pd.read_csv(file_path)
        elif ext in ['.xlsx', '.xls']:
            # 讀取 Excel
            df = pd.read_excel(file_path)
        else:
            raise ValueError("不支援的檔案格式！請上傳 csv 或 xlsx")

        # 2. 為了示範，我們先把資料轉成簡單的字串，並抓出前 5 筆
        # df.head() 是 pandas 用來抓前 5 筆資料的函式
        summary = f"成功讀取！\n資料總筆數: {len(df)}\n\n前 5 筆資料:\n{df.head().to_string()}"

        return summary

    except Exception as e:
        raise RuntimeError(f"讀取失敗: {e}")


def upload_file(self):
    file_path = filedialog.askopenfilename(filetypes=[("Excel/CSV", "*.xlsx;*.xls;*.csv")])

    if not file_path:
        return

    self.result_text.delete("0.0", "end")
    self.result_text.insert("0.0", f"正在讀取: {file_path}...\n")
    self.update()  # 強制刷新介面

    try:
        # 呼叫核心工具
        data_summary = load_data(file_path)

        self.result_text.delete("0.0", "end")
        self.result_text.insert("0.0", data_summary)
    except Exception as e:
        self.result_text.insert("end", f"錯誤: {e}")
