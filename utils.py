from config import Config
import json, os

def parse_config_file(file_path):
    try:
        with open(file_path, 'r') as file:
            config_data = json.load(file)

        # Check if any property is empty
        empty_properties = [key for key, value in config_data.items() if value == ""]
        if empty_properties:
            raise ValueError(f"The following properties in the config file are empty: {', '.join(empty_properties)}")

        # Create an instance of Config
        config_instance = Config(
            config_data['SPREADSHEETID'],
            config_data['SPREADSHEETNAME'],
            config_data['COLUMNRANGE']
        )
        
        return config_instance

    except FileNotFoundError:
        raise FileNotFoundError(f"Config file '{file_path}' not found.")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in the config file '{file_path}'.")

def check_credentials():
    """
    Check if a file called 'credentials.json' exists.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.exists("credentials.json")