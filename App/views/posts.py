from flask import Blueprint,render_template,flash,url_for,redirect,request,current_app
from App.forms import SendPosts
from App.models import Posts
from flask_login import current_user
posts=Blueprint('posts',__name__)
@posts.route('/send_posts/',methods=['GET','POST'])
def send_posts():
    form =SendPosts()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            p=Posts(title=form.articletitle.data,article=form.article.data,user=current_user)
            p.save()
            flash('发表成功')
            return redirect(url_for('posts.send_posts'))
        else:
            flash('您还没有登录，请先登录再发表')
    if not current_user.is_authenticated:
        flash('您还没有登录，请登录后再发表')
    return render_template('posts/send_posts.html',form=form)

@posts.route('/search/',methods=['POST'])
def search():
    try:
        page=int(request.args.get('page', 1))
    except:
        page=1
    keyword=request.form.get('search')
    # print(keyword)
    pagination=Posts.query.filter(Posts.title.contains(keyword)).paginate(page, current_app.config['EVERY_PAGE_NUM'],False)
    data=pagination.items

    return render_template('posts/search.html',data=data,pagination=pagination)



