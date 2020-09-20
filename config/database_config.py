import os

CONNECTION_CONFIG = {
    "host": os.environ.get('HOST'),
    "database": os.environ.get('DATABASE'),
    "user": os.environ.get('USER'),
    "password": os.environ.get('PASSWORD')
}
