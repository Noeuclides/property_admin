from .base import *

DEBUG = False


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',
        'OPTIONS': {
            'MAX_ENTRIES': 600000
        }
    }
}