import customtkinter as ctk
from core.logic import sample_test


class HydroCalcTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # --- 介面佈局 ---
        ctk.CTkLabel(self, text="合理化公式計算 (Q=CIA)", font=("微軟正黑體", 16, "bold")).pack(pady=10)

        # 輸入區
        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.pack(pady=5)

        self.entry_c = ctk.CTkEntry(self.input_frame, placeholder_text="逕流係數 (C)")
        self.entry_c.pack(pady=5)

        self.entry_i = ctk.CTkEntry(self.input_frame, placeholder_text="降雨強度 (I)")
        self.entry_i.pack(pady=5)

        self.entry_a = ctk.CTkEntry(self.input_frame, placeholder_text="集水面積 (A)")
        self.entry_a.pack(pady=5)

        # 結果標籤
        self.result_label = ctk.CTkLabel(self, text="準備計算...", font=("Arial", 14))
        self.result_label.pack(pady=10)

        # 計算按鈕 (綁定到 class 內部的方法)
        ctk.CTkButton(self, text="開始計算", command=self.perform_calculation).pack(pady=10)

    # --- 內部邏輯方法 ---
    def perform_calculation(self):
        try:
            val_c = float(self.entry_c.get())
            val_i = float(self.entry_i.get())
            val_a = float(self.entry_a.get())

            # 呼叫外部的核心邏輯
            result = sample_test.calculate_q(val_c, val_i, val_a)

            self.result_label.configure(text=f"計算結果: {result:.2f}", text_color="blue")
        except ValueError:
            self.result_label.configure(text="錯誤: 請輸入數字", text_color="red")
        except Exception as e:
            self.result_label.configure(text=f"未知錯誤: {e}", text_color="red")