def calculate_q(c, i, a):
    """
    純粹的數學計算，不涉及任何視窗介面。
    """
    # 這裡做邏輯檢查
    if not (0 < c <= 1.0):
        raise ValueError("逕流係數 (C) 必須在 0 到 1 之間")

    if i < 0 or a < 0:
        raise ValueError("數值不能為負數")

    # 回傳計算結果
    return c * i * a
