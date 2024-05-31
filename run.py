import logging
from api import app
from utils import parse_config_file, check_credentials

# Configure the logging
logging.basicConfig(level=logging.INFO,  # Set the logging level
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the log message format
                    handlers=[
                        # logging.FileHandler('app.log'),  # Log to a file
                        logging.StreamHandler()  # Also log to the console
                    ])

logger = logging.getLogger(__name__)  # Create a logger

# Check credentials
if check_credentials():
    logger.info("Credentials file exists.")
else:
    logger.warning("Credentials file does not exist.")

# Parse configuration file
config = parse_config_file('config.json')	

if __name__ == '__main__':
    app.config.from_object(config)
    logger.info("Starting the application.")
    app.run(host='0.0.0.0', port=80, debug=True)
