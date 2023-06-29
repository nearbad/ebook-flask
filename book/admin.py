from book import app
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField
from wtforms import validators


class BookView(ModelView):
    form_extra_fields = {
        'cover_image': FileUploadField('Обложка', base_path=app.config['UPLOADED_IMAGES_DEST'], validators=[validators.DataRequired()])
    }