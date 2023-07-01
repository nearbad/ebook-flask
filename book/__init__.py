import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_uploads import UploadSet, IMAGES
from flask_admin import Admin
from flask_uploads import configure_uploads


secret_key = os.urandom(32)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.db'
app.config['SECRET_KEY'] = secret_key
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)



# Создание экземпляра UploadSet для загрузки изображений
images = UploadSet('images', IMAGES)

# Конфигурация пути загрузки изображений
app.config['UPLOADED_IMAGES_DEST'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/uploads')
app.config['UPLOADED_IMAGES_URL'] = '/static/uploads'
# Конфигурация загрузчика изображений
configure_uploads(app, images)

from .admin import MyAdminIndexView

admin = Admin(app, index_view=MyAdminIndexView())
from book import routes

