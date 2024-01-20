"""Файл для удаления файла в облачном хранилище."""

from api.delete import delete
from logs.logs import context_logger


def missing_files(drive: dict, local: dict) -> None:
    """
    Функция, перманентно удаляющая файл.
    Получает на вход словари с файлами.
    Если списки файлов равны, фунции нет смысла работать дальше.
    При обнаружении в облачном хранилище файла, которого нет в локальном, удаляет его.
    В конце пишутся логи в зависимости от кода ответа.

    :param drive: файлы Яндекс диска
    :param local: локальные файлы
    """
    if drive.keys() == local.keys():
        return

    for file in drive.keys():
        if not local.get(file):
            answer = delete(file)

            if answer == 204:
                context_logger.info(f'Файл {file} успешно удален.')
            elif answer == 423:
                context_logger.error(f'Не удалось удалить файл {file}. Ведутся технические работы.')
            else:
                context_logger.error(f'Не удалось удалить файл {file}. Ошибка соединения.')
