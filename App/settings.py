import os

BASE_PATH=os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY='esdfghj'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    BOOTSTRAP_SERVE_LOCAL=True
    MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.qq.com')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME','2421983506@qq.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD','htwktcoqiwspebjh')
    MAX_CONTENT_LENGTH=1024*1024*64
    UPLOADED_PHOTOS_DEST=os.path.join(BASE_PATH,'static/upload/')
    EVERY_PAGE_NUM=3
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:s19930110l@127.0.0.1:3306/python1807'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    DEBUG=True
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:s19930110l@127.0.0.1:3306/test_python1807'
    DEBUG = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:s19930110l@127.0.0.1:3306/product_python1807'
    DEBUG = False
configDict={'default':DevelopmentConfig,
            'development':DevelopmentConfig,
            'testing':TestingConfig,
            'production':ProductionConfig}