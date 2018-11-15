from flask_classy import FlaskView, route


class UserView(FlaskView):
    # route_base = ''

    def login(self):
        return '欢迎登陆'

    def logout(self):
        return '退出登录'

    def profile(self):
        return '用户详情'

    @route('/register/')
    def enroll(self):
        return '欢迎注册'