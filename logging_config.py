import seqlog

def configure_logging():
    seqlog.configure_from_dict({
        'version': 1,  # Specify the configuration version
        'handlers': {
            'seq': {
                'class': 'seqlog.structured_logging.SeqLogHandler',
                'formatter': 'plain',
                'server_url': 'http://localhost:5341',  # Seq server URL
                'api_key': '',  # Optional Seq API key
                'batch_size': 10,  # Number of log messages to batch before sending
                'auto_flush_timeout': 10,  # Time in seconds before auto-flushing the batch
                'level': 'INFO',  # Minimum log level
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'plain',
                'level': 'INFO',  # Minimum log level for console
                'stream': 'ext://sys.stdout',  # Output to standard output
            },
        },
        'loggers': {
            '': {
                'level': 'INFO',
                'handlers': ['seq', 'console'],  # Add both handlers
            },
        },
        'formatters': {
            'plain': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
    })