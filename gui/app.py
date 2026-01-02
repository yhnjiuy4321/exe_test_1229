# gui/app.py
import customtkinter as ctk
import os
import core.utility
from gui.tabs import HydroCalcTab, FileReaderTab, ChannelTab
from core.configLoader import load_config


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # --- 基礎視窗設定 ---
        self.title('多功能工具箱 Pro')
        self.config = load_config()
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        w = self.config["window"]["width"]
        h = self.config["window"]["height"]
        self.geometry(f"{w}x{h}")

        # 設定圖示
        try:
            icon_path = core.utility.resource_path(os.path.join("assets", "doggy_16X16.ico"))
            self.iconbitmap(icon_path)

        except:
            pass

        # --- 建立 TabView ---
        self.tabview = ctk.CTkTabview(self, width=550, height=500)
        self.tabview.pack(padx=20, pady=20)

        # 新增分頁
        self.tabview.add("水文計算器")
        self.tabview.add("檔案讀取器")
        self.tabview.add("河道斷面分析")

        # --- 【關鍵】把剛剛拆出去的類別裝進來 ---

        # 1. 實體化水文計算器，並塞進 "水文計算器" 分頁
        self.hydro_view = HydroCalcTab(master=self.tabview.tab("水文計算器"))
        self.hydro_view.pack(fill="both", expand=True)

        # 2. 實體化檔案讀取器，並塞進 "檔案讀取器" 分頁
        self.file_view = FileReaderTab(master=self.tabview.tab("檔案讀取器"))
        self.file_view.pack(fill="both", expand=True)

        # 3. 實體化並放入
        # 注意：master 要指向 "河道斷面分析" 這個分頁
        self.channel_view = ChannelTab(master=self.tabview.tab("河道斷面分析"))
        self.channel_view.pack(fill="both", expand=True)

    def start(self):
        self.mainloop()
