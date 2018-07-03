# 导入视图类
from .main import MainView

# 将视图类统一放到元组中
DEFAULT_VIEWS = (MainView, )


# 注册视图类
def config_views(app):
    for view in DEFAULT_VIEWS:
        view.register(app)
