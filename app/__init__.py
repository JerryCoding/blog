from flask import Flask
from app.config import config
from app.views import config_views


def create_app(config_name):
    # 创建对象
    app = Flask(__name__)
    # 初始化配置
    config_class = config.get(config_name, 'default')
    app.config.from_object(config_class)
    config_class.init_app(app)
    # 配置视图类
    config_views(app)
    # 返回对象
    return app
