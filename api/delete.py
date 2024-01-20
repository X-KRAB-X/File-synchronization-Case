"""Файл, содержащий функцию для удаления."""

import requests
from config_data.config import TOKEN, DISK_PATH


def delete(file_name: str) -> int:
    """
    Функция для удаления файла с Яндекс диска.
    Отправляет запрос на удаление по указанному пути.

    :param file_name: Имя файла.
    :return: Код ответа.
    """
    response = requests.delete(f'https://cloud-api.yandex.net/v1/disk/resources?path={DISK_PATH}/{file_name}&'
                               f'permanently=true',
                               headers={"Accept": "application/json",
                                        'Authorization': TOKEN}
                               )
    return response.status_code
