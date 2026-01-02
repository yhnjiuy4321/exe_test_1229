# 檔案位置：gui/tabs/channel_tab.py
import customtkinter as ctk
import math

# --- 繪圖相關 ---
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import gui.plot_utils as plot_utils


class ChannelTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # 設定左右兩邊佈局：左邊(權重1)放輸入框，右邊(權重3)放圖表
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        # ==========================
        # 左側：控制面板 (輸入參數)
        # ==========================
        self.ctrl_frame = ctk.CTkFrame(self)
        self.ctrl_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        ctk.CTkLabel(self.ctrl_frame, text="曼寧公式計算", font=("微軟正黑體", 16, "bold")).pack(pady=10)

        # 建立輸入框
        self.entry_b = self.create_input("底寬 b (m)", "10")
        self.entry_z = self.create_input("邊坡 z (1:z)", "2")
        self.entry_y = self.create_input("水深 y (m)", "2.5")
        self.entry_n = self.create_input("曼寧 n", "0.025")
        self.entry_s = self.create_input("坡度 S", "0.001")

        # 計算按鈕
        self.btn_calc = ctk.CTkButton(self.ctrl_frame, text="計算並繪圖", command=self.calculate_and_plot)
        self.btn_calc.pack(pady=20)

        # 結果顯示區
        self.result_text = ctk.CTkTextbox(self.ctrl_frame, height=150)
        self.result_text.pack(pady=10, padx=5, fill="x")

        # ==========================
        # 右側：圖表顯示區
        # ==========================
        self.plot_frame = ctk.CTkFrame(self)
        self.plot_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # 初始化一張空白圖表
        self.init_plot()

    def create_input(self, text, default_val):
        """ 快速產生標籤+輸入框的輔助函式 """
        frame = ctk.CTkFrame(self.ctrl_frame, fg_color="transparent")
        frame.pack(pady=5, fill="x")
        ctk.CTkLabel(frame, text=text, width=80, anchor="w").pack(side="left", padx=5)
        entry = ctk.CTkEntry(frame)
        entry.insert(0, default_val)
        entry.pack(side="right", expand=True, fill="x", padx=5)
        return entry

    def init_plot(self):
        """ 設定 Matplotlib 圖表與 Tkinter 的連結 """
        # 1. 建立畫布 (Figure)
        # self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=100)
        self.fig, self.ax, self.canvas = plot_utils.create_figure(self.plot_frame)

        # 設定背景色配合 CTk 的深色/淺色模式 (這裡先用灰色)
        # self.fig.patch.set_facecolor('#f0f0f0')
        #
        # self.ax.set_title("Channel Cross Section")
        # self.ax.set_aspect('equal')  # 讓比例尺 1:1，圖形才不會變形
        # self.ax.grid(True, linestyle='--', alpha=0.6)
        #
        # # 2. 把畫布塞進 CTkFrame
        # self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        # self.canvas.draw()
        # self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def calculate_and_plot(self):
        try:
            # 1. 抓取數據
            b = float(self.entry_b.get())
            z = float(self.entry_z.get())
            y = float(self.entry_y.get())
            n = float(self.entry_n.get())
            s = float(self.entry_s.get())

            # 2. 數學計算 (曼寧公式)
            area = (b + z * y) * y  # 斷面積 A
            p = b + 2 * y * math.sqrt(1 + z ** 2)  # 濕周 P
            r = area / p  # 水力半徑 R
            v = (1 / n) * (r ** (2 / 3)) * (s ** 0.5)  # 流速 V
            q = area * v  # 流量 Q

            # 顯示文字結果
            res = f"斷面積 A = {area:.2f} m²\n流速 V = {v:.2f} m/s\n流量 Q = {q:.2f} cms"
            self.result_text.delete("0.0", "end")
            self.result_text.insert("0.0", res)

            # 3. 呼叫畫圖
            self.draw_channel(b, z, y)

        except ValueError:
            self.result_text.insert("0.0", "輸入錯誤：請輸入數字")

    def draw_channel(self, b, z, y):
        """ 畫出梯形斷面與水位 """
        self.ax.clear()  # 清除舊圖

        # 設定繪圖邊界
        top_width = b + 2 * z * y
        margin = max(2, top_width * 0.2)

        # --- 1. 畫河床 (棕色) ---
        # 座標順序：左上 -> 左底 -> 右底 -> 右上
        x_bed = [-(b / 2 + z * y * 1.5), -b / 2, b / 2, (b / 2 + z * y * 1.5)]
        y_bed = [y * 1.5, 0, 0, y * 1.5]

        self.ax.plot(x_bed, y_bed, 'k-', linewidth=2)  # 黑線
        self.ax.fill_between(x_bed, y_bed, color='#8B4513', alpha=0.3, label='河床')

        # --- 2. 畫水體 (藍色) ---
        x_water = [-(b / 2 + z * y), -b / 2, b / 2, (b / 2 + z * y)]
        y_water = [y, 0, 0, y]

        self.ax.fill_between(x_water, y_water, color='blue', alpha=0.5, label='水體')
        # 畫水面線
        self.ax.hlines(y, x_water[0], x_water[3], colors='blue', linestyles='--')
        self.ax.text(0, y, "▼", color='blue', ha='center', va='bottom', fontsize=12)

        # 設定標題與網格
        self.ax.set_title(f"Channel Section (Depth = {y}m)")
        self.ax.set_aspect('equal')
        self.ax.grid(True, linestyle=':', alpha=0.5)
        self.ax.legend()
        self.ax.set_xlim(-top_width / 2 - margin, top_width / 2 + margin)

        # 圖例放在外面
        self.ax.legend(loc='center left', bbox_to_anchor=(1.05, 0.5), borderaxespad=0)
        # self.fig.tight_layout(rect=[0, 0, 0.85, 1])  # 留出空間給圖例
        # self.fig.tight_layout(pad=3.0)
        # self.fig.tight_layout(pad=3.0)
        self.fig.subplots_adjust(left=0.1, right=0.75, top=0.9, bottom=0.1)

        # ★★★ 關鍵：自動調整版面 ★★★
        # self.fig.tight_layout()

        # 關鍵：更新畫布
        self.canvas.draw()
