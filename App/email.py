
from flask import render_template,current_app
from flask_mail import Message
from threading import Thread #导入线程模块
from App.extensions import mail



def send_mail_async(app,msg):
    #管理程序上下文
    with app.app_context():
        mail.send(message=msg)


def send_mail(subject,to,**kwargs):
    #拿到你实例化的 app对象
    app = current_app._get_current_object()
    msg = Message(subject=subject,recipients=[to],sender=app.config['MAIL_USERNAME'])
    msg.html = render_template('email/activate.html',**kwargs)
    thr = Thread(target=send_mail_async,args=(app,msg))
    thr.start() #开启线程
    # return '发送邮件'
# def change_mail_async(app,msg):
#     #管理程序上下文
#     with app.app_context():
#         mail.send(message=msg)
# def change_mail(subject,to,**kwargs):
#     #拿到你实例化的 app对象
#     app = current_app._get_current_object()
#     msg = Message(subject=subject,recipients=[to],sender=app.config['MAIL_USERNAME'])
#     msg.html = render_template('email/changeemail.html',**kwargs)
#     thr = Thread(target=send_mail_async,args=(app,msg))
#     thr.start() #开启线程
#     # return '发送邮件'




