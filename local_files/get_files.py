import os
from config_data.config import FILE_PATH


def get_files_list():
    return os.listdir(FILE_PATH)
