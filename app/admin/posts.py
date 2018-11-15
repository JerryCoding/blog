from flask_admin.contrib.sqlamodel import ModelView
from wtforms import TextAreaField
from wtforms.widgets import TextArea


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class PostsView(ModelView):
    can_delete = False
    column_exclude_list = ['content']
    column_labels = {
        'title': '标题',
        'content': '内容',
        'create_time': '创建时间',
        'praise': '赞',
        'negate': '踩',
        'category': '类别',
    }
    # 列表页显示的字段列表
    column_list = ['category', 'praise', 'negate', 'create_time', 'title', 'content']
    # 列表页可以更改的字段列表
    column_editable_list = ['category', 'title', 'content']

    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']

    form_overrides = {
        'content': CKTextAreaField
    }
