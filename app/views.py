from flask import render_template, redirect, request, url_for, flash, session
from app import app
from app.models.application import Application
from app.models.user import User

app_class = Application()


@app.route('/')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """"
    route to return the signup page and redirect to the login once registered successfully
    """
    error = None

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if username and email and password:
            user = User(username, email, password)
            if app_class.register(user):
                flash('You have been registered')
                return redirect(url_for('login'))
            error = 'User already exists'

    return render_template('signup.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """"
    route to login existing user and redirect them to home once logged in
    Errors are displayed in case of wrong credentials
    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email and password:
            if app_class.login(email, password):
                session['email'] = email
                return redirect(url_for('home'))
            error = 'Invalid credentials. Please try again'
            return render_template('login.html', error=error)

    return render_template('login.html')
