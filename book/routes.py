from flask import render_template, redirect, url_for, flash, request
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import func

from book import app, db, bcrypt, admin
from flask_login import login_user, logout_user

from .admin import BookView
from .models import User, Book
from .forms import RegisterForm, LoginForm


@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password1.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
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


admin.add_view(ModelView(User, db.session))
admin.add_view(BookView(Book, db.session))


def filter_books(genres=None, min_price=None, max_price=None):
    query = Book.query

    if genres:
        query = query.filter(Book.genre.in_(genres))

    if min_price is not None:
        query = query.filter(Book.price >= min_price)
    if max_price is not None:
        query = query.filter(Book.price <= max_price)

    books = query.all()
    return books


@app.route('/ebooks')
def all_books():
    min_price = db.session.query(func.min(Book.price)).scalar()
    max_price = db.session.query(func.max(Book.price)).scalar()
    selected_genres = request.args.getlist('genre')
    min_price_selected = request.args.get('min_price')
    max_price_selected = request.args.get('max_price')
    books = filter_books(genres=selected_genres, min_price=min_price_selected, max_price=max_price_selected)
    genres = ['Fantasy', 'Detective', 'Horror', 'Business', 'Romance']
    return render_template('books.html', books=books, genres=genres, min_price=min_price, max_price=max_price)


@app.route('/ebook/<int:book_id>')
def book_detail(book_id):
    book = Book.query.get(book_id)
    return render_template('book_detail.html', book=book)


@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query')
    print(query)
    if query:
        books = Book.query.filter(
            (Book.title.ilike(f'%{query}%')) |
            (Book.author.ilike(f'%{query}%'))
        ).all()
    else:
        books = []
    return render_template('search_results.html', books=books)


@app.route('/access_denied')
def access_denied():
    return render_template('access_denied.html')