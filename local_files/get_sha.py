import os
from config_data.config import FILE_PATH
from get_files import get_files_list
import hashlib


def get_sha_dict():
    files = get_files_list()
    hash_dict = {}

    for file in files:
        with open(os.path.join(FILE_PATH, file), 'rb') as data:
            text = data.read()
            file_hash = hashlib.sha256(text).hexdigest()
            hash_dict[file] = file_hash

    return hash_dict
