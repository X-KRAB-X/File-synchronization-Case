from api.delete import delete
from logs.logs import context_logger


def missing_files(drive, local):
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
