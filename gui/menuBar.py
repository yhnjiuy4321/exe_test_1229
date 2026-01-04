import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox  # 如果需要彈出訊息窗
import core.utility  # 假設你的 load_data 在這裡


def on_open():
    print("選單觸發：開啟舊檔")


def on_save():
    print("選單觸發：儲存檔案")


def on_exit(menu_bar):
    def exit_app():
        print("選單觸發：離開應用程式")
        menu_bar.winfo_toplevel().destroy()  # 關閉主視窗

    return exit_app


def show_file_menu(self):
    """ 顯示檔案選單 """
    try:
        # 取得按鈕的絕對位置
        x = self.btn_file.winfo_rootx()
        y = self.btn_file.winfo_rooty() + self.btn_file.winfo_height()

        # 在按鈕下方顯示選單
        self.popup_file_menu.tk_popup(x, y)
    finally:
        # 釋放抓取 (grab)
        self.popup_file_menu.grab_release()


def show_about_info():
    """ 顯示關於視窗 """
    messagebox.showinfo(
        title="關於 多功能工具箱 Pro",
        message="多功能工具箱 Pro\n版本 1.0\n作者: 你的名字\n© 2024 版權所有"
    )


class MenuBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        # 設定預設樣式：高度 40，深灰色背景，直角
        super().__init__(master, height=40, corner_radius=0, fg_color="#333333", **kwargs)

        # 1. 建立「檔案」按鈕
        self.btn_file = ctk.CTkButton(
            self,
            text="檔案 (File)",
            font=("微軟正黑體", 14, "bold"),
            fg_color="transparent",  # 透明背景
            # 字體顏色白色
            text_color="#FFFFFF",
            hover_color="#555",  # 滑鼠懸停色
            width=80,
            command=lambda: show_file_menu(self)  # 按下觸發彈出
            , corner_radius=0
        )
        self.btn_file.pack(side="left", padx=2)

        # self.winfo_toplevel()，確保選單綁定在主視窗上
        self.popup_file_menu = tk.Menu(self.winfo_toplevel(), tearoff=0, font=("微軟正黑體", 12))
        self.popup_file_menu.add_command(label="開啟舊檔", command=on_open)
        self.popup_file_menu.add_command(label="儲存檔案", command=on_save)
        self.popup_file_menu.add_separator()
        self.popup_file_menu.add_command(label="離開", command=on_exit(self))

        # 2. 建立「關於」按鈕
        self.btn_About = ctk.CTkButton(
            self,
            text="關於 (About)",
            font=("微軟正黑體", 14, "bold"),
            fg_color="transparent",  # 透明背景
            # 字體顏色白色
            text_color="#FFFFFF",
            hover_color="#555",  # 滑鼠懸停色
            width=100,
            command=show_about_info  # 按下觸發彈出
            , corner_radius=0
        )

        self.btn_About.pack(side="left", padx=2)
