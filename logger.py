import logging
import os
from datetime import datetime

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f"logs/videoxplore_{datetime.now().strftime('%Y%m%d')}.log"),
            logging.StreamHandler()
        ]
    )

setup_logger()
logger = logging.getLogger(__name__)

def log_info(message):
    logger.info(message)

def log_error(message, error=None):
    if error:
        logger.error(f"{message}: {str(error)}")
    else:
        logger.error(message)

def log_warning(message):
    logger.warning(message)

def log_debug(message):
    logger.debug(message)
