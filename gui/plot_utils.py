import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def setup_chinese_font():
    """ 全域設定：讓 Matplotlib 支援中文 """
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    plt.rcParams['axes.unicode_minus'] = False


def create_figure(master_frame, figsize=(5, 4), dpi=100):
    """
    通用函式：建立一個嵌入 Tkinter 的 Matplotlib 畫布

    參數:
        master_frame: 要把圖塞進去的那個容器 (Frame)
    回傳:
        fig: 畫布物件 (用來存檔或調整大小)
        ax:  座標軸物件 (用來畫圖 ax.plot)
        canvas: Tkinter 畫布元件 (用來 canvas.draw)
    """
    # 1. 確保字體設定正確
    setup_chinese_font()

    # 2. 建立畫布
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    fig.patch.set_facecolor('#f0f0f0')  # 背景色

    # 3. 建立 Canvas 並塞入介面
    canvas = FigureCanvasTkAgg(fig, master=master_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    return fig, ax, canvas
