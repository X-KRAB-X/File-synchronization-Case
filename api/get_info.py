"""Файл для получения файлов и их хеш-сумм из облачного хранилища."""

import requests
import time
from config_data.config import TOKEN, DISK_PATH
from logs.logs import context_logger


def get_info() -> dict | int:
    """
    Функция, отправляющая запрос на получение списка файлов.
    При этом, обрабатывает ошибки при указании токена и пути к папке на Яндекс диске.
    Также, не получив должного ответа от сервера, возвращает код 404.

    :return: Словарь, содержащий список файлов в виде ключей и их хеш-суммы в виде значений.
    """
    response = requests.get(url=f'https://cloud-api.yandex.net/v1/disk/resources?path={DISK_PATH}',
                            headers={"Accept": "application/json",
                                     'Authorization': TOKEN}
                            )
    if response.status_code == 404:
        context_logger.error('Ошибка! Указаная папка не найдена на Яндекс Диске.')
        time.sleep(5)
        exit()
    elif response.status_code == 401:
        context_logger.error('Ошибка! Неверно указан токен.')
        time.sleep(5)
        exit()

    response = response.json()

    if response.get('_embedded'):
        files_info = {}
        for file in response['_embedded']['items']:
            files_info[file['name']] = file['sha256']
        return files_info
    else:
        return 404
