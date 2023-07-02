# InkSpire - Simple Flask-based E-Book Selling Website

## Beta Version

You can visit the beta version of the site by clicking [here](http://inkspire.pythonanywhere.com/). Please note that this version is still under development and may contain bugs or unfinished features. Your feedback and suggestions are highly appreciated as we work towards improving InkSpire.


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Admin Panel](#admin-panel)
- [Payment](#payment)
- [Search](#search)
- [Environment Variables](#environment-variables)
- [License](#license)

## Introduction

InkSpire is a Flask-based website designed for selling electronic books. It serves as an educational project for portfolio purposes. Users can register and log in to the site, and it includes two main models: `User` and `Book`. An admin panel is available to manage these models, but only super users have access to it. The payment system is integrated using the Stripe API. Books can be filtered by genre and price. The site is named "InkSpire".

## Features

- User Registration and Login
- Book Selling Platform
- Admin Panel with Super User Access
- Stripe API Integration for Payments
- Genre and Price Filters for Books
- Book Search by Title and Author

## Installation

To install and run InkSpire on your local machine, follow these steps:

1. Clone the repository: `git clone https://github.com/nearbad/ebook.git`
2. Change into the project directory: `cd ebook`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Create a `.env` file in the project directory and set the following environment variables:
   - `STRIPE_PUBLIC_KEY`: Your Stripe public API key
   - `STRIPE_SECRET_KEY`: Your Stripe secret API key

## Usage

To start the InkSpire web application, run the following command:

```bash
python run.py
```
Open your web browser and visit http://localhost:5000 to access the InkSpire website.

## Admin Panel
The admin panel allows super users to manage the User and Book models. To access the admin panel, follow these steps:

1. Log in as a super user.
2. Go to the admin panel link: `http://localhost:5000/admin`

## Payment

InkSpire uses the Stripe API to handle payments. Ensure you have the correct Stripe API keys set as environment variables. Payments are secure and seamless, providing a smooth user experience.

## Search

Users can search for books based on their titles and authors. The search feature helps users find their desired books quickly and efficiently.

## Environment Variables

InkSpire uses the following environment variables:

`STRIPE_PUBLIC_KEY`: Your Stripe public API key

`STRIPE_SECRET_KEY`: Your Stripe secret API key

Ensure these variables are properly set in the .env file before running the application.

## License

This project is licensed under the MIT License.
