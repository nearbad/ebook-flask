from flask import render_template, redirect, url_for, flash, request
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


admin.add_view(BookView(Book, db.session))


@app.route('/ebooks')
def all_books():
    books = Book.query.all()
    return render_template('books.html', books=books)


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
