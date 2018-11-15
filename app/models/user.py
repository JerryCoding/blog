from app.extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    join_time = db.Column(db.DateTime, default=datetime.utcnow())

    @property
    def password(self):
        raise AttributeError('password属性不可读')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)