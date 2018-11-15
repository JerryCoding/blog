# 导入类库
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_moment import Moment
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_uploads import UploadSet, IMAGES
from flask_uploads import configure_uploads, patch_request_class
from flask_admin import Admin
from flask_babelex import Babel


# 创建对象
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
migrate = Migrate(db=db)
moment = Moment()
login_manager = LoginManager()
photos = UploadSet('photos', IMAGES)
admin = Admin(name='博客中心', template_mode='bootstrap3', subdomain='admin', url='')
babel = Babel()


# 初始化对象
def config_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app)
    moment.init_app(app)
    # 登录管理初始化
    login_manager.init_app(app)
    # 指定登录的端点
    login_manager.login_view = 'UserView:login'
    # 指定登录的提示信息
    login_manager.login_message = '需要登录才可访问'

    # 上传文件初始化
    configure_uploads(app, photos)
    patch_request_class(app, size=None)

    # 后台管理
    admin.init_app(app)
    from app.admin import config_admin
    config_admin(admin)

    # 汉化处理
    babel.init_app(app)
