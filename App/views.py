from flask import Blueprint, render_template, request, redirect, url_for, session
from App.models import *

blue = Blueprint('blog', __name__)


# 首页
@blue.route('/')
def user_index():
    contents = Content.query.all()
    classifications = Classification.query.all()
    return render_template('home/index.html', contents=contents, classifications=classifications)




# 后台登录
@blue.route('/admin/login/', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        # 接收客户端提交的参数
        username = request.form.get('username')
        userword = request.form.get('userpwd')
        # 验证登录是否能成功
        if username == 'lisi' and userword == '123456':
            res = redirect(url_for('blog.admin_index'))  # 重定向到index.html
            # 设置session
            session["username"] = username
            return res
        return 'login failed'
    return render_template('admin/login.html')


# 后台首页
@blue.route('/admin/index/')
def admin_index():
    # session获取
    count = len(Content.query.all())
    username = session.get('username', '')
    if username == '':
        res = redirect(url_for('blog.admin_login'))
        return res
    return render_template('admin/index.html', username=username, count=count)




# 后台文章
@blue.route('/admin/article/', methods=['GET', 'POST'])
def admin_article():
    # contents = Content.query.all()
    username = session.get('username', '')
    if username == '':
        res1 = redirect(url_for('blog.admin_login'))
        return res1
    # classifications = Classification.query.all()
    res = redirect(url_for('blog.admin_article_page', page=1))
    # return render_template('admin/article.html', contents=contents, username=username)
    return res





# 后台退出登录
@blue.route('/admin/deletelogin/')
def delete_login():
    res = redirect(url_for('blog.admin_login'))
    # 删除sessionss
    session.pop('username')
    return res

# 后台用户管理
@blue.route('/admin/manageuser/')
def manage_user():
    username = session.get('username', '')
    if username == '':
        res = redirect(url_for('blog.admin_login'))
        return res
    return render_template('admin/manage-user.html', username=username)

