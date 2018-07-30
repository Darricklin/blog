from flask import Blueprint,render_template,redirect,url_for,current_app
from App.forms import Uploadedphotos
from App.extensions import file,db
from PIL import Image
import os,random,string
from flask_login import current_user,login_required
center=Blueprint('center',__name__)
def random_name(suffix,length=32):
    Str = string.ascii_letters+string.digits
    return ''.join(random.choice(Str) for i in range(length))+'.'+suffix

#图片缩放函数
def img_zoom(path,width=200,height=200,prefix='s_'):
    img = Image.open(path)
    print(img.size)  # 获取图片的宽 高
    img.thumbnail((width, height))  # 重新设计尺寸
    pathSplit = os.path.split(path) # 将路径拆分成 路径和文件名
    newPath = os.path.join(pathSplit[0],prefix+pathSplit[1]) #将前缀进行拼接
    img.save(newPath)  # 保存图片 覆盖掉原来的图片
@center.route('/upload/',methods=['GET','POST'])
@login_required
def upload():
    form=Uploadedphotos()
    img_url = file.url('default.jpg')
    if form.validate_on_submit():
        photo=form.photo.data
        suffix=photo.filename.split('.')[-1]
        while True:
            newname=random_name(suffix)
            path=os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],newname)
            if not os.path.exists(path):
                break
        file.save(photo,name=newname)
        if current_user.icon != 'default.jpg':
            os.remove(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],current_user.icon))
            os.remove(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],'s_'+current_user.icon))
        img_zoom(path)
        current_user.icon=newname
        db.session.add(current_user)
        db.session.commit()
        img_url=file.url(current_user.icon)
    return render_template('owncenter/uploadphoto.html',form=form,img_url=img_url)