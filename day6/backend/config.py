

class Config():
    # some config as base
    
    pass

class developmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///our_db.sqlite3'
    SECRET_KEY = 'shhhhhh....... its very secret'
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'
    DEBUG = True

    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_HOST = 'localhost'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 0
    CACHE_KEY_PREFIX = 'myapp_'
    CACHE_DEFAULT_TIMEOUT = 120    

    MAIL_SERVER = "localhost"
    MAIL_PORT = 1025
    MAIL_DEFAULT_SENDER = "dont_reply@abc.com"

class celeryConfig():
    broker_url = 'redis://localhost:6379/1'
    result_backend = 'redis://localhost:6379/2'
    timezone = 'Asia/Kolkata'

class productionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = server db url

    pass

class testingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_db.sqlite3'
