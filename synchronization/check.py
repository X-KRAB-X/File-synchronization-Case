from api.get_info import get_info # файлы
from local_files.get_sha import get_sha_dict
from synchronization.missing_files import missing_files # 3 вида проверки
from synchronization.new_files import new_files
from synchronization.same_files import same_files
from time import sleep
from requests.exceptions import ConnectionError
from logs.logs import context_logger


def check(interval):
    try:
        local_files = get_sha_dict()
        drive_files = get_info()

        same_files(drive_files, local_files)
        new_files(drive_files, local_files)
        missing_files(drive_files, local_files)
    except ConnectionError:
        context_logger.error('Не удалось загрузить данные с сервера. Отсутствует подключение к интернету.')

    sleep(interval)
