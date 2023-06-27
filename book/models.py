import os
from book import db, login_manager, images, app
from book import bcrypt
from flask_login import UserMixin
from werkzeug.utils import secure_filename
from flask import current_app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(80), nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    cover_image = db.Column(db.String(255))

    def save_cover_image(self, image):
        if image and self.allowed_file(image.filename):
            # Генерируем безопасное имя файла
            filename = secure_filename(image.filename)
            # Сохраняем файл в директорию загрузок
            image_path = os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], filename)
            image.save(image_path)
            # Обновляем поле cover_image
            self.cover_image = image_path
            db.session.commit()

    @staticmethod
    def allowed_file(filename):
        # Проверяем расширение файла
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

    def image_url(self):
        if self.cover_image:
            return current_app.config['UPLOADED_IMAGES_URL'] + '/' + self.cover_image
        else:
            return None

