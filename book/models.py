from datetime import datetime
import os
from book import db, login_manager, images, app
from book import bcrypt
from flask_login import UserMixin
from werkzeug.utils import secure_filename
from flask import current_app, url_for


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(80), nullable=False)
    is_superuser = db.Column(db.Boolean, nullable=False, default=False)

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
    genre = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    cover_image = db.Column(db.String(255), nullable=True)
    file = db.Column(db.String(255), nullable=False)

    def save_cover_image(self, cover_image):
        if cover_image:
            filename = secure_filename(cover_image.filename)
            cover_image.save(os.path.join(app.config['UPLOADED_IMAGES_DEST'], filename))
            self.cover_image = filename

    def save_file(self, file):
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOADED_IMAGES_DEST'], filename))
            self.file = filename

    def image_url(self):
        if self.cover_image:
            return url_for('static', filename='uploads/' + self.cover_image)
        return None

    def file_url(self):
        if self.file:
            return url_for('static', filename='pdf/' + self.file)
        return None

