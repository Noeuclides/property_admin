from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    '0.0.0.0',
    'localhost',
]


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if not CONTAINER_RUNNING:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'property_db',
            'USER': 'property_user',
            'PASSWORD': 'property_pass',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
else:
    DATABASES = {
        'default': env.db()
    }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "public/static"),
    ]
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media/')
MEDIA_URL = '/media/'
