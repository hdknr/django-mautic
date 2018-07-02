DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'djmautic', 'USER': 'djmautic', 'PASSWORD': 'djmautic',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
ALLOWED_HOSTS = ['localhost', 'develop.local']
# URL_PREFIX = '/prtool'
URL_PREFIX = ''
STATIC_URL = f'{URL_PREFIX}/static/'            
