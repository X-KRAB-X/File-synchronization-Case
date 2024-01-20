"""Файл, содержащий функцию для отправки файла."""

import requests
from api.get_url import get_url


def load(path: str, file_name: str) -> int:
    """
    Функция для загрузки файла на Яндекс диск.
    Получает URL, по которому отправляет открытый в бинарном режиме файл.

    :param path: Путь к файлу в локальном хранилище.
    :param file_name: Имя файла.
    :return: Код ответа.
    """
    url = get_url(file_name)
    if url == 404:
        return 404

    file_to_load = open(path, 'rb')
    files = {'file': file_to_load}

    response = requests.post(url, files=files)
    file_to_load.close()
    return response.status_code
