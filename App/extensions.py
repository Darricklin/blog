from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager
from flask_cache import Cache
from flask_moment import Moment
from flask_uploads import UploadSet,IMAGES,configure_uploads,patch_request_class
#实例化各种第三方库
bootstrap=Bootstrap()
db=SQLAlchemy()
migrate=Migrate(db=db)
mail=Mail()
login_manager = LoginManager()
file = UploadSet('photos',IMAGES)
cache=Cache(config={'CACHE_TYPE':'redis'})
moment=Moment()
#把app在各种第三方库的实例中初始化
def config_extension(app):
    bootstrap = Bootstrap(app)
    db.init_app(app)
    migrate.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view= 'user_register.login'
    login_manager.login_message='您还没有登录，请先登录'
    login_manager.session_protection='strong'
    configure_uploads(app,file)
    patch_request_class(app,size=None)
    cache.init_app(app)
    moment.init_app(app)
