

class Config():
    # some config as base

    pass

class developmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///our_db.sqlite3'
    SECRET_KEY = 'shhhhhh....... its very secret'
    SECURITY_JOIN_USER_ROLES = True

class productionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = server db url

    pass

class testingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_db.sqlite3'
