import requests
from config_data.config import TOKEN, DISK_PATH


def get_url(file_name, overwrite=False):
    response = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={DISK_PATH}/{file_name}&'
                            f'overwrite={overwrite}',
                            headers={"Accept": "application/json",
                                     'Authorization': TOKEN}
                            ).json()

    if response.get('href'):
        return response['href']
    else:
        return 404
