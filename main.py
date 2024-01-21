"""Главный файл для запуска. Помимо этого, содержит проверку интервала на положительность."""

import time
from config_data.config import INTERVAL, FILE_PATH
from synchronization.check import check
import logs.logs


if __name__ == '__main__':
    if INTERVAL < 0:
        logs.logs.context_logger('Ошибка! Интервал должен быть больше 0.')
        time.sleep(5)
        exit()
    logs.logs.context_logger.info(f'Программа синхронизации файлов начинает работу с директорией {FILE_PATH}')
    while True:
        check(INTERVAL)
