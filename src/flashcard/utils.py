from pathlib import Path
from django.conf import settings
from decouple import Config,RepositoryEnv,config as decouple_config
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR.parent
ENV_FILE = PROJECT_DIR / '.env'

def conf():
    if ENV_FILE.exists():
        return Config(RepositoryEnv(ENV_FILE))
    return decouple_config


config = conf()
