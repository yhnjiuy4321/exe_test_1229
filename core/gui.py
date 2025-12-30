import tkinter as tk

# 負責跟「Python 直譯器」溝通的工具。
import sys

# 負責跟「電腦系統 (Windows)」溝通的工具。
import os


def on_button_click():
    global label
    label.config(text="按鈕已被按下！")


def close_button():
    global window
    window.destroy()


def resource_path(relative_path):
    """Get the absolute path to the resource, works for dev and PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def start_gui():
    global window, label
    window = tk.Tk()
    window.title('GUI')
    window.geometry('380x400')
    window.resizable(False, False)
    # window.iconbitmap('assets/doggy.ico')
    window.iconbitmap(resource_path('../assets/doggy_16X16.ico'))

    label = tk.Label(window, text="", font=("Arial", 12))
    label.pack(pady=20)

    test = tk.Button(window, text="測試", command=on_button_click)
    test.pack()

    test = tk.Button(window, text="關閉視窗", command=close_button)
    test.pack()

    # 給我兩個輸入框，一個是單行輸入框，一個是多行輸入框，輸入完按下計算可以算出相加值
    single_line_entry = tk.Entry(window, width=30)
    single_line_entry.pack(pady=10)
    multi_line_text = tk.Text(window, width=30, height=5)
    multi_line_text.pack(pady=10)

    def calculate_sum():
        try:
            num1 = float(single_line_entry.get())
            num2 = float(multi_line_text.get("1.0", tk.END).strip())
            result = num1 + num2
            label.config(text=f"相加結果：{result}")
        except ValueError:
            label.config(text="請輸入有效的數字！")

    calc_button = tk.Button(window, text="計算相加值", command=calculate_sum)
    calc_button.pack(pady=10)

    window.mainloop()
