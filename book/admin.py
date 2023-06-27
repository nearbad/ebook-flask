from flask_admin.contrib.sqla import ModelView
from flask_wtf.file import FileRequired
from wtforms import FileField


class BookView(ModelView):
    form_overrides = {
        'cover_image': FileField
    }

    form_args = {
        'cover_image': {
            'label': 'Cover Image',
            'validators': [FileRequired()],
        }
    }
