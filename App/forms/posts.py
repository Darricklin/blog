from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length

class SendPosts(FlaskForm):
    articletitle = StringField('标题',validators=[DataRequired(message='标题不能为空'),Length(min=1,max=20,message='标题长度为1～20个之间')],render_kw={'maxlength':20,'placeholder':'输入标题...'})
    article = TextAreaField('内容',validators=[DataRequired(message='内容不能为空...'),Length(min=10,max=2000,message='文章内容最大为10～2000字')],render_kw={'maxlength':2000,'placeholder':'输入博客内容...'})
    submit = SubmitField('发表')