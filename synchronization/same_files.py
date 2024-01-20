import os
from config_data.config import FILE_PATH
from api.reload import reload
from logs.logs import context_logger


def same_files(drive, local):
    for file in local.keys():
        if drive.get(file):
            if drive[file] != local[file]:
                answer = reload(os.path.join(FILE_PATH, file), file)

                if answer == 201:
                    context_logger.info(f'Файл {file} успешно перезаписан.')
                elif answer == 507:
                    context_logger.error(f'Не удалось перезаписать файл {file}. Недостаточно свободного места.')
                elif answer == 413:
                    context_logger.error(f'Не удалось перезаписать файл {file}. Файл слишком большой.')
                else:
                    context_logger.error(f'Не удалось перезаписать файл {file}. Ошибка соединения.')