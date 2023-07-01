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
        # elif not current_user.is_superuser:
        #     return redirect(url_for('access_denied'))
        return super(MyAdminIndexView, self).index()


class PdfFileValidator:
    def __call__(self, form, field):
        if field.data:
            if not field.data.filename.endswith('.pdf'):
                raise validators.ValidationError('Please upload a PDF file.')


class BookView(ModelView):
    form_extra_fields = {
        'cover_image': FileUploadField('Cover', base_path=app.config['UPLOADED_IMAGES_DEST'],
                                       validators=[validators.DataRequired()]),
        'file': FileUploadField('PDF', base_path=app.config['UPLOADED_PDFS_DEST'], validators=[
            validators.DataRequired(),
            PdfFileValidator()
        ])
    }
