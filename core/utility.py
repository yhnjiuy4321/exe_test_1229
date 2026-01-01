# 上傳讀取excel csv檔 給我程式碼
import os

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


def load_data(file_path):
    """
    讀取 CSV 或 Excel 檔案，並回傳資料
    回傳: (資料內容字串, 欄位清單)
    """
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





