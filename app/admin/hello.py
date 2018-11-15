from flask_admin import BaseView, expose


class HelloView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')



