import logging
from api import app
from utils import check_credentials
from logging_config import configure_logging

configure_logging()

logger = logging.getLogger(__name__)

if check_credentials():
    logger.info("Credentials file exists.")
else:
    logger.warning("Credentials file does not exist.")
if __name__ == '__main__':    
    logger.info("Starting the application.")
    app.run(host='0.0.0.0', port=80, debug=True)
