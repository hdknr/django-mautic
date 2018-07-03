DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'djmautic', 'USER': 'djmautic', 'PASSWORD': 'djmautic',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
    'mautic': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'mautic', 'USER': 'mautic', 'PASSWORD': 'mautic',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
}
URL_PREFIX = ''
STATIC_URL = f'{URL_PREFIX}/static/'            
