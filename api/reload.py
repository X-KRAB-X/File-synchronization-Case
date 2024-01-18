import requests
from get_url import get_url


def reload(path, file_name):
    url = get_url(file_name, overwrite=True)
    file_to_load = open(path, 'rb')
    files = {'file': file_to_load}

    response = requests.post(url, files=files)
    file_to_load.close()
