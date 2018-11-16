from flask import Flask
from app.config import config
from app.views import config_views
from app.extensions import config_extensions


def create_app(config_name):
    # 创建对象
    app = Flask(__name__)
    # 初始化配置
    if config_name not in config:
        config_name = 'default'
    app.config.from_object(config[config_name])
    # 添加扩展
    config_extensions(app)
    # 配置视图类
    config_views(app)
    # 返回对象
    return app
