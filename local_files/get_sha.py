"""Файл для высчитывания хеш-сумм всех локальных файлов."""

import os
import hashlib
from config_data.config import FILE_PATH
from local_files.get_files import get_files_list


def get_sha_dict() -> dict:
    """
    Функция, высчитывающая хеш-сумму каждого файла.

    :return: Словарь, содержащий список файлов в виде ключей и их хеш-суммы в виде значений.
    """
    files = get_files_list()
    hash_dict = {}

    for file in files:
        with open(os.path.join(FILE_PATH, file), 'rb') as data:
            text = data.read()
            file_hash = hashlib.sha256(text).hexdigest()
            hash_dict[file] = file_hash

    return hash_dict
