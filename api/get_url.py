"""Файл, содержащий функцию для получения ссылки на отправку файла."""

import requests
from config_data.config import TOKEN, DISK_PATH


def get_url(file_name: str, overwrite=False) -> str | int:
    """
    Функция, получающая ссылку для отправки файла на Яндекс диск.
    Посылает запрос с указаным путем будущего файла.
    В случае ошибки возвращает код 404.

    :param file_name: Имя файла.
    :param overwrite: Режим перезаписи.
    :return: Ссылка для отправки | код ошибки
    """
    response = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={DISK_PATH}/{file_name}&'
                            f'overwrite={overwrite}',
                            headers={"Accept": "application/json",
                                     'Authorization': TOKEN}
                            ).json()

    if response.get('href'):
        return response['href']
    else:
        return 404
