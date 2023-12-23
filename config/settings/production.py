import os

from .base import *
from decouple import config

# Config for Docker postgres connection
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_NAME"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": "localhost",
        # default port you don't need to mention in docker-compose
        "PORT": 5432,
    }
}
