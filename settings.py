import os

import dj_database_url
from dotenv import load_dotenv


load_dotenv()
SECRET_KEY = os.environ['SECRET_KEY']
DB_URL = os.environ['DB_URL']

DATABASES = {
    'default': dj_database_url.config(default=DB_URL)
}

INSTALLED_APPS = ['datacenter']

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
