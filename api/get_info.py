"""Файл для получения файлов и их хеш-сумм из облачного хранилища."""

import requests
from config_data.config import TOKEN, DISK_PATH


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
        exit('Ошибка! Указаная папка не найдена на Яндекс Диске.')
    elif response.status_code == 401:
        exit('Ошибка! Неверно указан токен.')

    response = response.json()

    if response.get('_embedded'):
        files_info = {}
        for file in response['_embedded']['items']:
            files_info[file['name']] = file['sha256']
        return files_info
    else:
        return 404
