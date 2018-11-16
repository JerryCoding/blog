from flask_classy import FlaskView
from flask import render_template
# from app.models import Posts, Category
# from app.extensions import db


class MainView(FlaskView):
    # route_base = ''

    def index(self):
        return render_template('common/base.html')


    def create(self):
        # p1 = Posts(title='flask入门', content='xxx', cid=1)
        # p2 = Posts(title='flask视图', content='yyy', cid=1)
        # p3 = Posts(title='flask模板', content='zzz', cid=1)
        # p4 = Posts(title='flask模型', content='www', cid=1)
        # db.session.add_all([p2, p3, p4])
        return '数据已添加'