from .settings import *

#PROJECT_DIR = ROOT_DIR.path('project')

SECRET_KEY = 'CHANGEME!!!'
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

#MEDIA_ROOT = str(PROJECT_DIR.path('test_media'))
