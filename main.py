"""Главный файл для запуска. Помимо этого, содержит проверку интервала на положительность."""

from config_data.config import INTERVAL, FILE_PATH
from synchronization.check import check
import logs.logs


if __name__ == '__main__':
    if INTERVAL < 0:
        exit('Ошибка! Интервал должен быть больше 0.')
    logs.logs.context_logger.info(f'Программа синхронизации файлов начинает работу с директорией {FILE_PATH}')
    while True:
        check(INTERVAL)
