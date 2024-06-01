import seqlog
import colorlog

def configure_logging():
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
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'colored',
                'level': 'INFO',
                'stream': 'ext://sys.stdout',
            },
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
            },
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
            },
        },
    })