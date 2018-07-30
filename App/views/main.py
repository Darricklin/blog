from flask import Blueprint,render_template,redirect,url_for,request,current_app
from App.models import Posts
from flask_login import current_user
main=Blueprint('main',__name__)
from App.extensions import cache
@main.route('/')
def index():
    return redirect(url_for('main.show',page=1))
@main.route('/show/<int:page>/',methods=['GET','POST'])
#设置数据缓存，如果客户请求首页，会将首页视图函数，html等数据缓存到客户本地浏览器，提高客户下次请求的
#响应速度，同时降低服务器处理请求的次数，缓解服务器压力。
@cache.memoize(timeout=60)#缓存数据保存时间为60秒
def show(page):
    print('-------------------------------')
    pagination=Posts.query.filter(Posts.pid==0).order_by(Posts.timestamp.desc()).paginate(page,
               current_app.config['EVERY_PAGE_NUM'],False)
    data = pagination.items
    list=['朝天炮','花季少女','金满天']
    return render_template('main/index.html',data=data,pagination=pagination,list=list)
@main.route('/personal/')
def personal():
    try:
        page=int(request.args.get('page', 1))
    except:
        page=1
    pagination=Posts.query.filter(Posts.uid==current_user.id).order_by(Posts.timestamp.desc()).paginate(page,
               current_app.config['EVERY_PAGE_NUM'],False)
    data=pagination.items
    return  render_template('main/personal.html',data=data,pagination=pagination)


