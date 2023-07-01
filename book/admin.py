from flask import redirect, url_for
from flask_admin import AdminIndexView, expose
from book import app
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField
from wtforms import validators
from flask_login import current_user


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('access_denied'))
        elif not current_user.is_superuser:
            return redirect(url_for('access_denied'))
        return super(MyAdminIndexView, self).index()


class BookView(ModelView):
    form_extra_fields = {
        'cover_image': FileUploadField('Обложка', base_path=app.config['UPLOADED_IMAGES_DEST'], validators=[validators.DataRequired()])
    }


