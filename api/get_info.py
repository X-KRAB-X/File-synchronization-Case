import requests
from config_data.config import TOKEN, DISK_PATH


def get_info() -> dict:
    response = requests.get(url=f'https://cloud-api.yandex.net/v1/disk/resources?path={DISK_PATH}',
                            headers={"Accept": "application/json",
                                     'Authorization': TOKEN}
                            )
    if response.status_code == 404:
        exit('Ошибка! Указаная папка не найдена на Яндекс Диске.')
    elif response.status_code == 401:
        exit('Ошибка! Неверно указан токен.')

    response = response.json()
    files_info = {}

    for file in response['_embedded']['items']:
        files_info[file['name']] = file['sha256']

    return files_info
