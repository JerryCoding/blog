from flask_admin.contrib.sqlamodel import ModelView
from flask_admin import form
from jinja2 import Markup
from flask import url_for, current_app
from sqlalchemy.event import listens_for
from app.models import Category
import os


file_path = os.getcwd()
file_path = os.path.join(file_path, 'app/static/upload')


class CategoryView(ModelView):

    # 设置缩略图的
    def list_thumbnail(self, context, model, name):
        if not model.icon:
            return ''

        return Markup('<img src="%s" width="20">' % url_for('static',
                                                 filename='upload/'+model.icon))

    # 格式化列表的图像显示
    column_formatters = {
        'icon': list_thumbnail
    }

    # 扩展列表显示的头像为60*60像素
    form_extra_fields = {
        'icon': form.ImageUploadField('Image',
                                          base_path=file_path,
                                          thumbnail_size=(60, 60, True))
    }
    # show columns in edit or create page
    form_columns = ('name', 'icon')

# 监听删除事件，删除类别顺便把对应类别的图片也删除，包括缩略图
@listens_for(Category, 'after_delete')
def del_image(mapper, connection, target):
    if target.icon:
        # Delete image
        try:
            os.remove(os.path.join(file_path, target.icon))
        except OSError:
            pass

        # Delete thumbnail
        try:
            os.remove(os.path.join(file_path,
                              form.thumbgen_filename(target.icon)))
        except OSError:
            pass