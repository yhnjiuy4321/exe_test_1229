def calculate_q(c: float, i: float, a: float) -> float:
    """
    計算流量
    :param c: 逕流係數 (0.0 ~ 1.0)
    :param i: 降雨強度 (mm/hr)
    :param a: 面積 (ha)
    :return: 流量 CMS
    """
    if not (0 < c <= 1.0):
        raise ValueError("逕流係數 (C) 必須在 0 到 1 之間")

    if i < 0 or a < 0:
        raise ValueError("數值不能為負數")

    # 回傳計算結果
    return c * i * a
