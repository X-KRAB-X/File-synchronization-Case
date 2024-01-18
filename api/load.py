import requests
# from config_data.config import FILE_PATH
# import os
from get_url import get_url


def load(path, file_name):
    url = get_url(file_name)
    file_to_load = open(path, 'rb')
    files = {'file': file_to_load}

    response = requests.post(url, files=files)
    file_to_load.close()


# load(os.path.join(FILE_PATH, '123.txt'), '123.txt')
