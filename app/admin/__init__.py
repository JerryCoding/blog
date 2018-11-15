from app.models import Posts, Category
from app.extensions import db
from .hello import HelloView
from .posts import PostsView
from .category import CategoryView


def config_admin(admin):
    admin.add_view(HelloView(name='Hello 1', endpoint='hello1', category='Test'))
    admin.add_view(HelloView(name='Hello 2', endpoint='hello2', category='Test'))
    admin.add_view(HelloView(name='Hello 3', endpoint='hello3', category='Test'))

    admin.add_view(PostsView(Posts, db.session, name='博客'))
    admin.add_view(CategoryView(Category, db.session, name='类别'))
