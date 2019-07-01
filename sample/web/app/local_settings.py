import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'mautic': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'bpmt', 'USER': 'bpmt', 'PASSWORD': 'bpmt',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
}
URL_PREFIX = ''
STATIC_URL = f'{URL_PREFIX}/static/'            
MAUTIC = {
    'base': 'http://localhost:8000/ma',
}
ALLOWED_HOSTS = ['develop.local'] 