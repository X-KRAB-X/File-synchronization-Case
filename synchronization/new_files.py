"""Файл для загрузки нового файла в облачное хранилище."""

import os
from config_data.config import FILE_PATH
from api.load import load
from logs.logs import context_logger


def new_files(drive: dict, local: dict) -> None:
    """
    Функция, загружающая новый файл в облачное хранилище.
    Получает на вход словари с файлами.
    Если списки файлов равны, фунции нет смысла работать дальше.
    При обнаружении в локальном хранилище файла, котороге нет в облачном, загружает его.
    В конце пишутся логи в зависимости от кода ответа.

    :param drive: файлы Яндекс диска
    :param local: локальные файлы
    """
    if drive.keys() == local.keys():
        return

    for file in local.keys():
        if not drive.get(file):
            answer = load(os.path.join(FILE_PATH, file), file)

            if answer == 201:
                context_logger.info(f'Файл {file} успешно загружен.')
            elif answer == 507:
                context_logger.error(f'Не удалось загрузить файл {file}. Недостаточно свободного места.')
            elif answer == 413:
                context_logger.error(f'Не удалось загрузить файл {file}. Файл слишком большой.')
            elif answer == 423:
                context_logger.error(f'Не удалось загрузить файл {file}. Ведутся технические работы.')
            elif answer == 410:
                continue
            else:
                context_logger.error(f'Не удалось загрузить файл {file}. Ошибка соединения.')
