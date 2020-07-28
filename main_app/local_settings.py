import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'erasysdb2',
#         'USER': 'postgres',
#         'PASSWORD': '123456',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     },
# }

# import dj_database_url

# db_config = dj_database_url.config()
# if db_config:
#     DATABASES['default'] =  db_config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'erasysdb',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'db',
        'PORT': '',
    },
}
