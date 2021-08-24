import os
import env


class DevelopmentConfig:
    DEBUG = True

    user = env.flask_db_user
    password = env.flask_db_password
    host = env.flask_db_host
    dbname = env.flask_db_name
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{password}@{host}/{dbname}?charset=utf8'

    SQLALCHEMY_TRACE_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig