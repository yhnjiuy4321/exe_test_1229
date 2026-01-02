import logging
import os


def setup_logger():
    logging.basicConfig(
        filename='app_debug.log',  # 錯誤會存在這個檔案
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding='utf-8'
    )
    return logging.getLogger()


# logger 使用範例
# logger = setup_logger()
# logger.info("Logger 已初始化")
# logger.error("這是一個錯誤訊息範例")
# logger.debug("這是一個除錯訊息範例")
# logger.warning("這是一個警告訊息範例")
# logger.critical("這是一個嚴重錯誤訊息範例")
# logger.info(f"當前工作目錄: {os.getcwd()}")

# try:
#     # ... 計算 ...
# except Exception as e:
#     logging.error(f"計算發生嚴重錯誤: {e}") # 這會被記在檔案裡

