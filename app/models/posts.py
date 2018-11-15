from app.extensions import db
from datetime import datetime


# 帖子模型
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), unique=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    praise = db.Column(db.Integer, default=0)
    negate = db.Column(db.Integer, default=0)
    cid = db.Column(db.Integer, db.ForeignKey('category.id'))


# 类别模型
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True)
    icon = db.Column(db.String(64), unique=True)
    posts = db.relationship('Posts', backref='category', lazy='dynamic')

    # 关联显示时使用
    def __repr__(self):
        return self.name
