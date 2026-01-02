import customtkinter as ctk
from tkinter import filedialog
import core.utility  # 假設你的 load_data 在這裡


class FileReaderTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # --- 介面佈局 ---
        ctk.CTkLabel(self, text="數據分析工具", font=("微軟正黑體", 16, "bold")).pack(pady=10)

        # 上傳按鈕
        ctk.CTkButton(self, text="📂 上傳檔案", command=lambda: core.utility.upload_file(self)).pack(pady=10)

        # 顯示結果的 Textbox
        self.result_text = ctk.CTkTextbox(self, width=500, height=100)
        self.result_text.pack(pady=10, padx=10)
        self.result_text.insert("0.0", "請點擊上方按鈕上傳檔案...\n")

