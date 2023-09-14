from dj_database_url import config as dj_config
from .utils import config 

DATABASE_URL = config('DATABASE_URL')

DATABASES = {

    'default':dj_config(default=DATABASE_URL,conn_health_checks=True,conn_max_age=1000)

}