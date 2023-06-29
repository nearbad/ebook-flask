import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_uploads import UploadSet, IMAGES
from flask_admin import Admin
from flask_uploads import configure_uploads
from werkzeug.utils import secure_filename


secret_key = os.urandom(32)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.db'
app.config['SECRET_KEY'] = secret_key
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
admin = Admin(app)

# Создание экземпляра UploadSet для загрузки изображений
images = UploadSet('images', IMAGES)

# Конфигурация пути загрузки изображений
app.config['UPLOADED_IMAGES_DEST'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/uploads')
app.config['UPLOADED_IMAGES_URL'] = '/static/uploads'
# Конфигурация загрузчика изображений
configure_uploads(app, images)

from book import routes

