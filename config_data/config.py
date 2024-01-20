import os
from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены, так как отсутствует файл .env")
else:
    load_dotenv()

TOKEN = os.getenv('TOKEN')
FILE_PATH = os.getenv('FILE_PATH')
DISK_PATH = os.getenv('DISK_PATH')
INTERVAL = int(os.getenv('INTERVAL'))
