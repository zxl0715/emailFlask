import logging
#https://blog.csdn.net/zywvvd/article/details/87857816
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(filename='app.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

logger.addHandler(file_handler)

logging.info('开始打印日志！')
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")
