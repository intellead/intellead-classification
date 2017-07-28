import os
from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['DATABASE_NAME'], os.environ['DATABASE_USER'], os.environ['DATABASE_PASSWORD'], os.environ['DATABASE_HOST'], os.environ['DATABASE_PORT'])
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get('DATABASE_NAME'),
        "USER": os.environ.get('DATABASE_USER'),
        "PASSWORD": os.environ.get('DATABASE_PASSWORD'),
        "HOST": os.environ.get('DATABASE_HOST'),
        "PORT": os.environ.get('DATABASE_PORT'),
    }
}