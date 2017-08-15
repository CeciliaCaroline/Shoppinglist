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


@app.route('/home')
def home():
    """"
    Route with the user profile
    user is able to see the number of lists that they have
    """
    user = app_class.get_user(session['email'])

    if not user:
        flash('You need to login first')
        return redirect(url_for('login'))
    lists = user.total_lists()
    return render_template('home.html', user=user, lists=lists)


@app.route('/view/list')
def shopping_list():
    """"
    route to view shopping lists that have been created by the user.
    If none have been created, some text is displayed
    """
    error = None
    user = app_class.get_user(session['email'])
    if not user:
        flash('You need to login first')
        return redirect(url_for('login'))

    lists = user.get_lists()
    return render_template('shopping_list.html', lists=lists, error=error, user=user)


@app.route('/add/list', methods=['POST'])
def add_list():
    pass


@app.route('/edit/list/<listt_id>', methods=['POST', 'GET'])
def edit_list(list_id):
    pass


@app.route('/delete/list/<list_id>', methods=['GET', 'POST'])
def delete_list():
    pass


@app.route('/view/list/item/<listt_id>', methods=['POST', 'GET'])
def items():
    pass

@app.route('/logout')
def logout():
    """"
    route to log out user
    """
    session.pop('email', None)
    flash('You have been logged out')
    return redirect(url_for('login'))
