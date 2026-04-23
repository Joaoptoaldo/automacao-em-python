import logging
from dotenv import load_dotenv

def load_env() -> None:
    """Carrega variáveis de ambiente do .env"""
    load_dotenv()

def setup_logger(name, log_file='automacao.log') -> logging.Logger:
    """Configura logger"""
    logging.basicConfig(filename=log_file, level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(name)

def log_info(logger, msg) -> None:
    logger.info(msg)
    print(msg)

if __name__ == '__main__':
    load_env()
    logger: logging.Logger = setup_logger('test')
    log_info(logger, 'Helpers carregados!')

