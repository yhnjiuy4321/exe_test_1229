import tkinter as tk
def on_button_click():
    label.config(text="按鈕已被按下！")

def close_button():
    window.destroy()

import sys
import os

def resource_path(relative_path):
    """Get the absolute path to the resource, works for dev and PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

window = tk.Tk()
window.title('GUI')
window.geometry('380x400')
window.resizable(False, False)
# window.iconbitmap('assets/doggy.ico')
window.iconbitmap(resource_path('assets/doggy_16X16.ico'))

label = tk.Label(window, text="", font=("Arial", 12))
label.pack(pady=20)

test = tk.Button(window, text="測試", command=on_button_click)
test.pack()

test = tk.Button(window, text="關閉視窗", command=close_button)
test.pack()

window.mainloop()
