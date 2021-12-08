import os
from uuid import uuid4


class Config:
    SECRET_KEY = os.environ.get("SECRET", str(uuid4()))
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
