from settings.common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Database configuration
DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'frinat_test'
DATABASE_USER = 'frinat_test'
DATABASE_PASSWORD = '9ef4f216'

# Server configuration
PORT = 14618

INSTALLED_APPS += (
    'south',
)

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'frinat'
EMAIL_HOST_PASSWORD = '478hbf6fh3'
EMAIL_USE_TLS = False

SERVER_EMAIL = 'django-errors@fribourg-natation.ch'

GOOGLE_MAPS_API_KEY = 'ABQIAAAAHQfs1_Yhx7yAZYnymmWgpRQd37xxEEIlk3sZjl-Gh8OqxrV0TRSQsJmBd5dqUROwRWRmZo1Pp4IWmA'