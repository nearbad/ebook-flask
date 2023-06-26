from flask import render_template, redirect, url_for, flash, request
from book import app, db, bcrypt
from flask_login import login_user, logout_user
from .models import User, Book
from .forms import RegisterForm, LoginForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password1.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    if form.errors is not None:
        for error in form.errors.values():
            flash(f"There was an error while creating a user: {error}", category="danger")
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                flash('You have been logged in!', category='success')
                return redirect(url_for('index'))
            else:
                flash('Username or password incorrect.', category='danger')
        else:
            flash('Username or password incorrect.', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    flash('You have been logged out!', category='info')
    logout_user()
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/books/create', methods=['POST', 'GET'])
def create_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        description = request.form.get('description')
        price = float(request.form.get('price'))
        cover_image = request.files['cover_image']

        new_book = Book(title=title, author=author, description=description, price=price, cover_image=cover_image)
        new_book.save_cover_image(app, cover_image)
        flash('Book created!', category='success')
        return redirect(url_for('index'))
    else:
        return render_template('create_book.html')

