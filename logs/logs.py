"""Файл для создания логов. В программе используется отформатированная версия - context_logger"""

from loguru import logger

logger.add('logs.log', format='{extra[program_name]} {time} {level} {message}')
context_logger = logger.bind(program_name='Synchronization System')
