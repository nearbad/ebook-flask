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


class PdfFileValidator:
    def __call__(self, form, field):
        if field.data:
            if not field.data.filename.endswith('.pdf'):
                raise validators.ValidationError('Please upload a PDF file.')


class BookView(ModelView):
    column_searchable_list = ['title', 'author']  # Определение столбцов, по которым можно выполнять поиск

    # Определение метода для ограничения количества слов в поле описания
    def _description_formatter(view, context, model, name):
        max_chars = 50  # Максимальное количество символов для отображения
        description = getattr(model, name)
        truncated_description = description[:max_chars] + '...' if len(description) > max_chars else description
        return truncated_description

    # Назначение ограниченного форматтера для поля описания
    column_formatters = {
        'description': _description_formatter,
        'file': _description_formatter,
        'cover_image': _description_formatter,
    }

    form_extra_fields = {
        'cover_image': FileUploadField('Cover', base_path=app.config['UPLOADED_IMAGES_DEST'],
                                       validators=[validators.DataRequired()]),
        'file': FileUploadField('PDF', base_path=app.config['UPLOADED_PDFS_DEST'], validators=[
            validators.DataRequired(),
            PdfFileValidator()
        ])
    }
