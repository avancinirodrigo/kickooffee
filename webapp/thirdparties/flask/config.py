
import os


class Config:
    SERVER_URL = os.environ.get('SERVER_URL') or 'http://127.0.0.1:5000'
    DB_URL = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:postgres@localhost:5432/kickooffeedb'
    JWT_SECRET_KEY = 'supersecret'
