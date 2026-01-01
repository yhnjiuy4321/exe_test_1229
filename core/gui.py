from tkinter import filedialog
import customtkinter as ctk
import sys
import os
from core.logic import sample_test
import core.utility


# --- 邏輯函式維持不變 ---
def click_calculate(a, b, c, label):  # 把 label 傳進來，不要用 global
    try:
        val_a = float(a.get())
        val_b = float(b.get())
        val_c = float(c.get())
        result = sample_test.calculate_q(val_a, val_b, val_c)
        label.configure(text=f"計算結果: {result:.2f}", text_color="blue")
    except ValueError as ve:
        label.configure(text=f"錯誤: 請輸入數字", text_color="red")
    except Exception as e:
        label.configure(text=f"未知錯誤: {e}", text_color="red")


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# --- 主程式 ---
def start_gui():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    window = ctk.CTk()
    window.title('多功能工具箱')
    window.geometry('600x550')  # 稍微加大一點
    # window.configure(fg_color="#E0F7FA") # 如果你想改背景色要用 fg_color

    # 設定圖示
    try:
        icon_path = resource_path(os.path.join("assets", "doggy_16X16.ico"))
        window.iconbitmap(icon_path)
    except:
        pass

    # ==========================================
    # 使用 TabView (分頁) 來管理介面
    # ==========================================
    # 建立分頁容器
    tabview = ctk.CTkTabview(window, width=550, height=500)
    tabview.pack(padx=20, pady=20)

    # 建立兩個分頁
    tab_calc = tabview.add("水文計算器")
    tab_file = tabview.add("檔案讀取器")

    # ==========================================
    # 分頁 1: 水文計算器 (原本的計算功能)
    # ==========================================
    # 注意：所有的 master 都要改成 tab_calc

    ctk.CTkLabel(tab_calc, text="合理化公式計算 (Q=CIA)", font=("微軟正黑體", 16, "bold")).pack(pady=10)

    # 輸入區 (用 Frame 包起來比較整齊)
    input_frame = ctk.CTkFrame(tab_calc, fg_color="transparent")
    input_frame.pack(pady=5)

    entry1 = ctk.CTkEntry(input_frame, placeholder_text="逕流係數 (C)");
    entry1.pack(pady=5)
    entry2 = ctk.CTkEntry(input_frame, placeholder_text="降雨強度 (I)");
    entry2.pack(pady=5)
    entry3 = ctk.CTkEntry(input_frame, placeholder_text="集水面積 (A)");
    entry3.pack(pady=5)

    # 結果標籤
    result_label = ctk.CTkLabel(tab_calc, text="準備計算...", font=("Arial", 14))
    result_label.pack(pady=10)

    # 計算按鈕
    ctk.CTkButton(tab_calc, text="開始計算",
                  command=lambda: click_calculate(entry1, entry2, entry3, result_label)).pack(pady=10)

    # ==========================================
    # 分頁 2: 檔案讀取器 (原本消失的那一塊)
    # ==========================================
    # 注意：所有的 master 都要改成 tab_file

    ctk.CTkLabel(tab_file, text="數據分析工具", font=("微軟正黑體", 16, "bold")).pack(pady=10)

    # 上傳按鈕
    def on_upload_click():
        file_path = filedialog.askopenfilename(filetypes=[("Excel/CSV", "*.xlsx;*.xls;*.csv")])
        if file_path:
            result_text.delete("0.0", "end")
            result_text.insert("0.0", f"正在讀取: {file_path}...\n")
            window.update()

            try:
                # 這裡呼叫你的 utility
                data_summary = core.utility.load_data(file_path)
                result_text.delete("0.0", "end")
                result_text.insert("0.0", data_summary)
            except Exception as e:
                result_text.insert("end", f"錯誤: {e}")

    ctk.CTkButton(tab_file, text="📂 上傳檔案", command=on_upload_click).pack(pady=10)

    # 顯示結果的 Textbox
    result_text = ctk.CTkTextbox(tab_file, width=500, height=300)
    result_text.pack(pady=10, padx=10)
    result_text.insert("0.0", "請點擊上方按鈕上傳檔案...\n")

    window.mainloop()