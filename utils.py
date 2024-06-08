import os

def check_credentials():
    """
    Check if a file called 'credentials.json' exists.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.exists("credentials.json")