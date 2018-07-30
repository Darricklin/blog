from App.extensions import db
from datetime import datetime

class Base:
    #添加一条数据
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
    #添加多条数据
    @staticmethod
    def save_all(*args):
        try:
            db.session.add_all(args)
            db.session.commit()
        except:
            db.session.rollback()
    #自定义删除基类
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()

"""
id
title
article
pid
path
time
dianzan
count
uid
"""
class Posts(Base,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(23),index=True)
    article = db.Column(db.Text)
    pid = db.Column(db.Integer,default=0)
    path = db.Column(db.Text,default='0,')
    fabulous = db.Column(db.Integer,default=0)
    times = db.Column(db.Integer,default=0)
    timestamp = db.Column(db.DateTime,default=datetime.utcnow)
    #使用ForeignKey 来创建表的外键 作用是 和数据库中的user表(用户信息表)进行关联查询 表迁移以后 表中救会有一个 uid的字段  一对多 关系 一个用户 发表多个帖子 多的表使用ForeignKey 来关联1的一方
    #uid是模型Posts下的posts表单中的外键，关联的是User模型下的user表单中的id值，通过id值就可以找到对应的用户名，知道文章或评论是谁发的。
    uid = db.Column(db.Integer,db.ForeignKey('user.id'))