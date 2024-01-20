from config_data.config import FILE_PATH
import os
from api.load import load
from logs.logs import context_logger


def new_files(drive, local) -> None:
    if drive.keys() == local.keys():
        return

    for file in local.keys():
        if not drive.get(file):
            answer = load(os.path.join(FILE_PATH, file), file)

            if answer == 201:
                context_logger.info(f'Файл {file} успешно загружен.')
            elif answer == 507:
                context_logger.error(f'Не удалось загрузить файл {file}. Недостаточно свободного места.')
            elif answer == 413:
                context_logger.error(f'Не удалось загрузить файл {file}. Файл слишком большой.')
            else:
                context_logger.error(f'Не удалось загрузить файл {file}. Ошибка соединения.')
