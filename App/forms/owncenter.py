from flask_wtf import  FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField,FileAllowed,FileRequired
from App.extensions import file
class Uploadedphotos(FlaskForm):
    photo=FileField('上传头像',validators=[FileRequired(message='请上传头像'),FileAllowed(file,message='文件格式不正确')])
    submit=SubmitField('上传')