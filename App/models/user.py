from App.extensions import db
from werkzeug.security import check_password_hash,generate_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Seralize
from flask import current_app
from App.extensions import login_manager
from flask_login import UserMixin
#定义一个Base类对数据库进行操作
class Base:
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
    @staticmethod
    def save_all(*args):
        try:
            db.session.add_all(args)
            db.session.commit()
        except:
            db.session.rollback()
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
#定义一个User类，用于创建表单模型，
class User(UserMixin,Base,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(12),unique=True,index=True)
    userpass_hash=db.Column(db.String(128))
    sex=db.Column(db.Boolean,default=True)
    birth = db.Column(db.String(20))
    email=db.Column(db.String(50))
    icon = db.Column(db.String(40), default='default.jpg')
    confirm=db.Column(db.Boolean,default=False)
    #给User模型设置一个外键接口，对接Posts模型与User模型下的user表，采用带参数（dynamic）的方式对接。
    posts=db.relationship('Posts',backref='user',lazy='dynamic')
    #用property和setter的方法将方法变成像属性一样可以被调用，方便对其进行赋值，比较，判断等。
    @property
    #将password变成属性，当调用User.password时，抛出错误，让密码不可读。
    def password(self):
        raise AttributeError('密码不可读')
    @password.setter
    #给password属性设置方法，将用户输入的密码进行hash加密。
    def password(self,userpass):
        self.userpass_hash=generate_password_hash(userpass)
    #定义检查密码的方法
    def check_password(self,password):
        return check_password_hash(self.userpass_hash,password)
    #定义生成token的方法
    def generate_token(self):
        #用字符串作为参数将Seralize实例化，
        s = Seralize(current_app.config['SECRET_KEY'])
        #调用dumps方法以数据id为令牌，生成加密字符串；token为json类型.
        return s.dumps({'id':self.id})
    @staticmethod
    def check_token(token):
        #用同样的字符串生成构造token时完全一样的实例化对象。
        s=Seralize(current_app.config['SECRET_KEY'])
        #在能得到token的情况下try
        try:
            #用实例化对象解析邮箱传递给路由的token。得到Dict。
            Dict=s.loads(token)
            #取出Dict的id。
            id=Dict['id']
            #查找数据库中是否存在这个id，如果存在，u为True，否则为Flase。
            u=User.query.get(id)
            if not u:
                #如果不存在，抛出错误，不再执行后续代码。
                raise ValueError
        #得不到token就except
        except:
            #得不到token就返回错误
            return False
        #得到了token，并且解析到数据库中有对应的id。并且激活状态为Flase时，执行下列代码。
        if not u.confirm:
            #更改激活状态并保存
            u.confirm = True
            u.save()
        #随便返回一个真值，让其他情况下代码正常运行。
        return True

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
