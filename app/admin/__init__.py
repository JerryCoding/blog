from app.models import Posts, Category
from app.extensions import db
from .hello import HelloView
from .posts import PostsView
from .category import CategoryView
from flask_admin import AdminIndexView, expose, Admin
from flask_login import UserMixin, current_user
from flask import redirect, url_for, request


# 主页视图
class MyAdminIndexView(AdminIndexView, UserMixin):
    # 增加这个必须要登录后才能访问，不然显示403错误
    # 但是还是不许再每一个函数前加上这么判定的  ，不然还是可以直接通过地址访问
    def is_accessible(self):
        return current_user.is_authenticated

    # 跳转
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('UserView:login', next=request.url))

    # 后台首页
    @expose('/')
    def index(self):
        return self.render('admin/index.html')


def config_admin(app):
    admin = Admin(app, name='博客中心', template_mode='bootstrap3', subdomain='admin', url='',
                  index_view=MyAdminIndexView(url='/'))
    admin.add_view(HelloView(name='Hello 1', endpoint='hello1', category='Test'))
    admin.add_view(HelloView(name='Hello 2', endpoint='hello2', category='Test'))
    admin.add_view(HelloView(name='Hello 3', endpoint='hello3', category='Test'))

    admin.add_view(PostsView(Posts, db.session, name='博客'))
    admin.add_view(CategoryView(Category, db.session, name='类别'))
