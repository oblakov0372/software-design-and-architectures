import sys
from loguru import logger


def logging_setup():
    format_info = "<white>{time:HH:mm:ss.SS}</white> | <level>{level}</level> | <level>{message}</level>"
    logger.remove()

    logger.add(sys.stdout, colorize=True, format=format_info, level="DEBUG")


logging_setup()
