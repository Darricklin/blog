from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,RadioField,DateField
from wtforms.validators import Email,EqualTo,DataRequired,Length,ValidationError
from App.models import User
from .test import InputButtonField
from sqlalchemy import or_
from werkzeug.security import check_password_hash

class Register(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(message='用户名不能为空'),Length(min=6,max=12, message='用户名长度6~12位')
    ],render_kw={'placeholder':'请输入用户名','maxlength':12})
    userpass = PasswordField('密码', validators=[DataRequired(message='密码不能为空'), Length(min=6,max=20, message='密码长度为6~20位')
                                              ], render_kw={'placeholder': '请输入密码','maxlength':20})
    userpass1 = PasswordField('确认密码', validators=[EqualTo('userpass',message='两次输入密码不一致')], render_kw={'placeholder': '请再次输入密码','maxlength':20})
    # sex=RadioField('sex', choices=[(True,'男'),(False,'女')],default='m')
    # birth=DateField('出生日期',validators=[DataRequired(message='请填写生日')],render_kw={
    #     'placeholder':'例如：2001-01-01'})
    email=StringField('邮箱',validators=[DataRequired(message='请输入邮箱地址'),Email(message='请输入正确的邮箱地址'),Length(8,50,message='请输入正确的邮箱')],render_kw={
        'placeholder':'请输入正确的邮箱地址','maxlength':50})
    submit=SubmitField('提交')
    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已存在')
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已存在')
class Login(FlaskForm):
    username = StringField('用户名',
                           validators=[DataRequired(message='用户名不能为空')
                                       ], render_kw={'placeholder': '用户名 邮箱', 'maxlength': 50})
    userpass = PasswordField('密码',
                             validators=[DataRequired(message='密码不能为空'), Length(min=6, max=20, message='密码长度为6~20位')
                                         ], render_kw={'placeholder': '请输入密码', 'maxlength': 20})
    submit = SubmitField('登录')
    def validate_username(self,field):
        if not User.query.filter(or_(User.username==field.data,User.email==field.data)).first():
            raise ValidationError('该用户不存在！')



    # def validate_userpass(self,field):
    #     if not User.check_password(password=):
    #         raise ValidationError('密码不正确！')
class Changeuserpass(FlaskForm):
    userpass = PasswordField('原密码',
                             validators=[DataRequired(message='密码不能为空'), Length(min=6, max=20, message='密码长度为6~20位')
                                         ], render_kw={'placeholder': '请输入密码', 'maxlength': 20})
    newpass = PasswordField('新密码',
                            validators=[DataRequired(message='密码不能为空'), Length(min=6, max=20, message='密码长度为6~20位')
                                        ], render_kw={'placeholder': '请输入密码', 'maxlength': 20})
    againpass = PasswordField('确认密码', validators=[EqualTo('newpass', message='两次输入密码不一致')],
                              render_kw={'placeholder': '请再次输入密码', 'maxlength': 20})
    submit = SubmitField('修改')
class Changeemail(FlaskForm):
    userpass = PasswordField('密码',
                             validators=[DataRequired(message='密码不能为空'), Length(min=6, max=20, message='密码长度为6~20位')
                                         ], render_kw={'placeholder': '请输入密码', 'maxlength': 20})
    email = StringField('邮箱', validators=[DataRequired(message='请输入正确的邮箱地址'), Email(message='请输入正确的邮箱地址'),
                                          Length(8, 50, message='请输入正确的邮箱')], render_kw={
        'placeholder': '请输入新的邮箱地址', 'maxlength': 50})
    send=InputButtonField('发送邮件',validators=[DataRequired(message='请发送后提交')])
    checknum=StringField('验证码',render_kw={'placeholder':'请输入验证码','maxlength':6})
    submit = SubmitField('修改')