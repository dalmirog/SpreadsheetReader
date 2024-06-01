import logging
import seqlog

def configure_logging():
    # Initialize logging handlers
    handlers = {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'colored',
            'level': 'INFO',
            'stream': 'ext://sys.stdout',
        }
    }
    
    try:
        # Try to configure Seq logging
        seqlog.configure_from_dict({
            'version': 1,
            'handlers': {
                'seq': {
                    'class': 'seqlog.structured_logging.SeqLogHandler',
                    'formatter': 'plain',
                    'server_url': 'http://localhost:5341',
                    'api_key': '',
                    'batch_size': 10,
                    'auto_flush_timeout': 10,
                    'level': 'INFO',
                }
            },
            'loggers': {
                '': {
                    'level': 'INFO',
                    'handlers': ['seq', 'console'],
                },
            },
            'formatters': {
                'plain': {
                    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                }
            }
        })
        # If successful, add Seq handler to the list of handlers
        handlers['seq'] = seqlog.get_logger().handlers[0]
    except Exception as e:
        # Log the exception and continue with console logging
        logging.error(f"Error configuring Seq logging: {e}")
    
    # Configure logging using the defined handlers
    logging.config.dictConfig({
        'version': 1,
        'handlers': handlers,
        'loggers': {
            '': {
                'level': 'ERROR',  # Set the root logger level to ERROR
                'handlers': list(handlers.keys()),  # Use all defined handlers
            },
        },
        'formatters': {
            'colored': {
                '()': 'colorlog.ColoredFormatter',
                'format': '%(asctime)s - %(name)s - %(log_color)s%(levelname)s%(reset)s - %(message)s',
                'log_colors': {
                    'DEBUG': 'cyan',
                    'INFO': 'green',
                    'WARNING': 'yellow',
                    'ERROR': 'red',
                    'CRITICAL': 'bold_red',
                },
                'secondary_log_colors': {
                    'message': {
                        'DEBUG': 'cyan',
                        'INFO': 'green',
                        'WARNING': 'yellow',
                        'ERROR': 'red',
                        'CRITICAL': 'bold_red',
                    }
                },
                'reset': True,
                'style': '%'
            }
        }
    })