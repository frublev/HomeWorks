import logging
import os
import hashlib


def logger_func(path):
    def logger_decor(old_function):
        logger = logging.getLogger('functions')
        logger.setLevel(logging.INFO)
        filename = os.path.join(path, 'functions.log')
        handler = logging.FileHandler(filename)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        def new_function(*args, **kwargs):
            logger.info('Start' + ' ' + old_function.__name__ + ' with arguments: ' + str(args) + ' ' + str(kwargs))
            result = old_function(*args, **kwargs)
            logger.info('Finish with result' + ' ' + str(result))
            return result

        return new_function

    return logger_decor


@logger_func('D:\\PycharmProjects\\Netology')
def output_hash(file_name):
    with open(file_name) as read_file:
        for line in read_file:
            yield hashlib.md5(line.encode()).digest()


if __name__ == '__main__':
    for line_h in output_hash("country-link.txt"):
        print(line_h)
