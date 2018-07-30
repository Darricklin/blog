from App.forms import Register,Login,Changeuserpass,Changeemail
from flask import Blueprint,render_template,flash,redirect,url_for
from App.models import User
from App.email import send_mail
from flask_login import login_user,logout_user,login_required,current_user
from sqlalchemy import or_

user=Blueprint('user', __name__)


@user.route('/register/',methods=['GET','POST'])
def register():
    form = Register()
    # form.hidde.data = 'hiddenvalue'
    if form.validate_on_submit():
        u = User(username=form.username.data,password=form.userpass.data,email=form.email.data)
        u.save()
        token=u.generate_token()
        send_mail('账户激活',u.email,username=u.username,token=token)
        return redirect(url_for('user.login'))
    return render_template('user/register.html',form=form)
@user.route('/activate/<token>/')
def activate(token):
    #调用校验token的方法  激活成功或者失败
    if User.check_token(token):
        return redirect(url_for('user.login'))
    else:
        flash('激活失败 请重新点击激活码 进行账户的激活')
        return redirect(url_for('user.register'))
@user.route('/login/',methods=['GET','POST'])
def login():
    form=Login()
    if form.validate_on_submit():
        u=User.query.filter(or_(User.username==form.username.data,User.email==form.username.data)).first()
        if not u.confirm:
            return '该用户还没有激活，请激活后登录'
        elif not u.check_password(form.userpass.data):
            return '密码输入错误'
        else:
            flash('登录成功,欢迎'+u.username)
            login_user(u)
            return redirect(url_for('main.index'))
    return render_template('user/login.html',form=form)
@user.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
@user.route('/center/')
@login_required
def center():
    return '必须登录才能访问'
@user.route('/changeuserpass/',methods=['GET','POST'])
@login_required
def changeuserpass():
    form = Changeuserpass()
    if form.validate_on_submit():
        u = current_user
        if not u.check_password(form.userpass.data):
            return '密码输入错误'
        else:
            u.password=form.newpass.data
            u.save()
            flash('修改成功')
            return redirect(url_for('main.index'))
    return render_template('user/changeuserpass.html',form=form)
@user.route('/changeemail/',methods=['GET','POST'])
@login_required
def changeemail():
    form = Changeemail()
    if form.validate_on_submit():
        u = current_user
        if not u.check_password(form.userpass.data):
            return '密码输入错误'
        else:
            u.email=form.email.data
            token = u.generate_token()
            send_mail('新邮箱激活', u.email, token=token)
            u.confirm = False
            if not u.confirm:
                u.save()
                return redirect(url_for('user.logout'))
    return render_template('user/changeemail.html',form=form)
# @user.route('/newemail/<token>/')
# def newemail(token):
#     if token:



