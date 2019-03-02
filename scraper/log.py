import logging


def logger():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] [%(filename)s > %(funcName)s]: %(message)s')
