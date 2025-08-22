# InkSpire
**A modern Flask-based E-Book Marketplace**
![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey?style=flat&logo=flask)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python)
![Stripe](https://img.shields.io/badge/Stripe-Integrated-635BFF?style=flat&logo=stripe)
![License](https://img.shields.io/badge/License-MIT-green.svg)
## 🚀 Live Demo (Beta)
Explore the live beta version of InkSpire: [http://inkspire.pythonanywhere.com/](http://inkspire.pythonanywhere.com/)
> **Note:** This is a beta version under active development. You may encounter unfinished features or bugs. We greatly appreciate your feedback and suggestions!
## 📖 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Admin Panel](#-admin-panel)
- [Payment Integration](#-payment-integration)
- [Search & Filtering](#-search--filtering)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [API Endpoints](#-api-endpoints)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
## 📋 Overview
InkSpire is a full-featured e-commerce platform built with Flask, designed specifically for selling digital books. This project serves as an educational demonstration of web development best practices, including user authentication, payment processing, and admin management.
The platform features two core models (`User` and `Book`) and provides a seamless experience for both customers and administrators.
## ✨ Key Features
- **👤 User Management**: Secure registration and login system
- **📚 E-Book Catalog**: Browse and purchase digital books
- **🛒 Shopping Cart**: Intuitive cart system for book purchases
- **🎛️ Admin Dashboard**: Full CRUD operations for superusers
- **🔒 Secure Payments**: Stripe integration for safe transactions
- **🔍 Advanced Search**: Find books by title or author
- **🎚️ Smart Filtering**: Filter by genre and price range
- **📱 Responsive Design**: Optimized for desktop and mobile devices
## 🛠️ Installation & Setup
### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git
### Step-by-Step Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/nearbad/ebook.git
   cd ebook
   ```
2. **Create and activate a virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   # Activate it (Windows)
   venv\Scripts\activate
    
   # Activate it (macOS/Linux)
   source venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Environment Configuration**
   Create a `.env` file in the project root:
   ```env
   # Stripe API Keys (Required)
   STRIPE_PUBLIC_KEY=your_stripe_public_key_here
   STRIPE_SECRET_KEY=your_stripe_secret_key_here
    
   # Flask Configuration (Optional but recommended)
   SECRET_KEY=your_very_secret_key_here
   DEBUG=True
   ```
5. **Database Setup** (if applicable)
   ```bash
   # Initialize database (if your project uses Flask-Migrate)
   flask db init
   flask db migrate
   flask db upgrade
   ```
## 🚀 Usage
### Starting the Development Server
```bash
python run.py
```
### Accessing the Application
1. Open your browser and navigate to `http://localhost:5000`
2. Register a new account or log in with existing credentials
3. Browse the book catalog and use search/filter features
4. Add books to your cart and proceed to checkout
### Creating a Superuser (if applicable)
```bash
flask shell
>>> from app import db, User
>>> admin = User(username='admin', email='admin@example.com', is_superuser=True)
>>> admin.set_password('password123')
>>> db.session.add(admin)
>>> db.session.commit()
```
## 👨‍💻 Admin Panel
Superusers can access the admin panel to manage site content:
1. Log in with superuser credentials
2. Navigate to `http://localhost:5000/admin`
3. Manage users, books, and other database entities
**Admin Features:**
- User management (create, edit, delete users)
- Book catalog management
- Order viewing and management
- Site analytics and reporting
## 💳 Payment Integration
InkSpire uses **Stripe** for secure payment processing:
### Setup Requirements
1. Create a Stripe account at [stripe.com](https://stripe.com)
2. Obtain API keys from Stripe Dashboard
3. Add keys to your `.env` file:
   ```env
   STRIPE_PUBLIC_KEY=pk_test_your_public_key_here
   STRIPE_SECRET_KEY=sk_test_your_secret_key_here
   ```
### Testing Payments
Use these test card numbers in development:
- Card: `4242 4242 4242 4242` | Exp: Any future date | CVC: Any 3 digits
- Success: `4000000000003220` (3D Secure)
- Failure: `4000000000009995`
## 🔍 Search & Filtering
InkSpire provides powerful search and filtering capabilities:
### Search
- Search books by title or author name
- Real-time search suggestions
- Case-insensitive matching
### Filtering
- Filter by genre/category
- Filter by price range
- Sort by price, title, or date added
- Combined search and filtering
## ⚙️ Configuration
### Environment Variables
| Variable | Description | Required |
|----------|-------------|----------|
| `STRIPE_PUBLIC_KEY` | Stripe publishable key for frontend | Yes |
| `STRIPE_SECRET_KEY` | Stripe secret key for backend operations | Yes |
| `SECRET_KEY` | Flask secret key for session security | Recommended |
| `DEBUG` | Enable/disable debug mode (True/False) | Optional |
| `DATABASE_URL` | Database connection URL | If using database |
### File Structure
```
ebook/
├── app/
│   ├── templates/      # HTML templates
│   ├── static/         # CSS, JS, images
│   ├── __init__.py     # Flask app initialization
│   ├── models.py       # Database models
│   ├── routes.py       # Application routes
│   └── utils.py        # Helper functions
├── venv/               # Virtual environment
├── .env                # Environment variables
├── requirements.txt    # Python dependencies
└── run.py              # Application entry point
```
## 📁 Project Structure
```
inkspire/
├── app/
│   ├── static/
│   │   ├── css/        # Stylesheets
│   │   ├── js/         # JavaScript files
│   │   └── images/     # Image assets
│   ├── templates/
│   │   ├── base.html   # Base template
│   │   ├── index.html  # Home page
│   │   ├── auth/       # Authentication templates
│   │   ├── books/      # Book-related templates
│   │   └── admin/      # Admin panel templates
│   ├── __init__.py     # Flask application factory
│   ├── models.py       # SQLAlchemy models
│   ├── routes.py       # Main application routes
│   ├── auth.py         # Authentication routes
│   ├── admin.py        # Admin panel routes
│   └── utils.py        # Utility functions
├── migrations/         # Database migrations (if using Flask-Migrate)
├── instance/           # Instance folder for configuration
├── tests/              # Unit tests
├── venv/               # Virtual environment
├── requirements.txt    # Dependencies
├── .env                # Environment variables
├── .gitignore         # Git ignore rules
└── run.py             # Application entry point
```
## 🌐 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page |
| GET | `/books` | Book catalog |
| GET | `/book/<id>` | Book details |
| POST | `/search` | Search books |
| GET | `/admin` | Admin dashboard |
| GET | `/register` | User registration form |
| POST | `/register` | Create new user |
| GET | `/login` | Login form |
| POST | `/login` | User authentication |
| GET | `/logout` | User logout |
| POST | `/create-checkout-session` | Create Stripe checkout session |
## 🐛 Troubleshooting
### Common Issues
1. **ModuleNotFoundError**
   ```bash
   # Ensure all dependencies are installed
   pip install -r requirements.txt
   ```
2. **Stripe keys not working**
   - Verify keys are correctly set in `.env`
   - Ensure Stripe account is activated
3. **Database issues**
   ```bash
   # Reinitialize database (if using Flask-Migrate)
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
4. **Port already in use**
   ```bash
   # Kill process on port 5000 (Unix-based systems)
   lsof -ti:5000 | xargs kill
   ```
## 🤝 Contributing
We welcome contributions to InkSpire! Please follow these steps:
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request
### Development Guidelines
- Follow PEP 8 style guide for Python code
- Add comments for complex logic
- Write tests for new functionality
- Update documentation accordingly
## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
