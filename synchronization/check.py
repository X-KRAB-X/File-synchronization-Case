"""Главый файл для сравнения файлов из обоих хранилищ."""

from time import sleep
from requests.exceptions import ConnectionError
from api.get_info import get_info
from local_files.get_sha import get_sha_dict
from logs.logs import context_logger
from synchronization.missing_files import missing_files
from synchronization.new_files import new_files
from synchronization.same_files import same_files


def check(interval: int) -> None:
    """
    Функция проверки.
    Получает 2 словаря с файлами и их sha256 хеш-суммами: Локальные и облачные соответственно.
    Если не удалось получить файлы с Яндекс диска, прекращает свою работу до следующей "итерации".
    Далее следует 3 проверки: Изменения в файлах(файлы с одним названием), новые файлы в локальном хранилище,
    лишние файлы в облачном.
    В случае отсутствия интернета ошибка обрабатывается и пишутся логи.

    :param interval: Интервал времени для пауз между проверками.
    """
    try:
        local_files = get_sha_dict()
        drive_files = get_info()
        if drive_files == 404:
            raise ConnectionRefusedError

        same_files(drive_files, local_files)
        new_files(drive_files, local_files)
        missing_files(drive_files, local_files)
    except ConnectionError:
        context_logger.error('Отсутствует подключение к интернету.')
    except ConnectionRefusedError:
        context_logger.error('Не удалось загрузить данные с сервера.')
    finally:
        sleep(interval)
