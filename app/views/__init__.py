# 导入视图类
from .main import MainView
from .user import UserView

# 将视图类统一放到元组中
DEFAULT_VIEWS = (
    # (类名, route_base)
    (MainView, '/'),
    (UserView, '/user'),
)


# 注册视图类
def config_views(app):
    for view, route_base in DEFAULT_VIEWS:
        view.register(app, route_base=route_base, subdomain='www')
