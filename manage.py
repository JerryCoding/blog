import os
from app import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand

config_name = os.getenv('FLASK_CONFIG', 'default')
app = create_app(config_name)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# 后台管理
from app.admin import config_admin
config_admin(app)


if __name__ == '__main__':
    manager.run()
