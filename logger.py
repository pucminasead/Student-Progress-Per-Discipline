import logging

# Criação do objeto logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Definição do formato de log
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

# Criação do manipulador de log para arquivo com bloqueio para evitar duplicação de mensagens
file_handler = logging.FileHandler(
    "./logs/logs.log", mode="a", encoding="utf-8", delay=True
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Adicionar o manipulador ao logger
logger.addHandler(file_handler)


def log_message_error(message):
    logger.error(message)


def log_message_info(message):
    logger.info(message)
