from flask_classy import FlaskView


class MainView(FlaskView):
    route_base = ''

    def index(self):
        return '博客中心'
