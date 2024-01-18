import requests
from config_data.config import TOKEN, DISK_PATH


def get_info() -> dict:
    response = requests.get(url=f'https://cloud-api.yandex.net/v1/disk/resources?path={DISK_PATH}',
                            headers={"Accept": "application/json",
                                     'Authorization': TOKEN}
                            ).json()
    files_info = {}

    for file in response['_embedded']['items']:
        files_info[file['name']] = file['sha256']

    return files_info
