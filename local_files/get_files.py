"""Файл для получения списка файлов в локальном хранилище."""

import os
import time
from config_data.config import FILE_PATH
from logs.logs import context_logger


def get_files_list() -> list:
    """
    Функция, возвращающая список файлов.
    Также обрабатывает ошибку и прекращает работу программы в случае неправильно указанного пути.

    :return: Список файлов.
    """
    try:
        return os.listdir(FILE_PATH)
    except FileNotFoundError:
        context_logger.error('Ошибка! Неправильно указан путь к отслеживаемой папке.')
        time.sleep(5)
        exit()
