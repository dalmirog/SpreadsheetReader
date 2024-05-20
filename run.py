from api import app
from utils import parse_config_file, check_credentials

if check_credentials():
    print("Credentials file exists.")
else:
    print("Credentials file does not exist.")
    
config = parse_config_file('config.json')	

if __name__ == '__main__':	
	app.config.from_object(config)
	app.run(host='0.0.0.0', port=80, debug = True)