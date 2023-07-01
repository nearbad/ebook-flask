import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_uploads import UploadSet, IMAGES, DOCUMENTS
from flask_admin import Admin
from flask_uploads import configure_uploads
from dotenv import load_dotenv

# Загрузка параметров из файла .env
load_dotenv()

secret_key = os.urandom(32)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ebook.db'
app.config['SECRET_KEY'] = secret_key
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Создание экземпляра UploadSet для загрузки файлов
images = UploadSet('images', IMAGES)
pdfs = UploadSet('pdfs', DOCUMENTS)

# Конфигурация пути загрузки изображений
app.config['UPLOADED_IMAGES_DEST'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/uploads')
app.config['UPLOADED_IMAGES_URL'] = '/static/uploads'

# Конфигурация пути загрузки PDF файлов
app.config['UPLOADED_PDFS_DEST'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/pdf')
app.config['UPLOADED_PDFS_URL'] = '/static/pdf'

# Конфигурация загрузчика файлов
configure_uploads(app, images)
configure_uploads(app, pdfs)

from .admin import MyAdminIndexView

admin = Admin(app, index_view=MyAdminIndexView(), template_mode='bootstrap4', base_template='admin/base.html')

from book import routes
