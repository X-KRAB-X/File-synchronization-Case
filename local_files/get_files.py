import os
from config_data.config import FILE_PATH


def get_files_list():
    try:
        return os.listdir(FILE_PATH)
    except FileNotFoundError:
        exit('Ошибка! Неправильно указан путь к отслеживаемой папке.')

