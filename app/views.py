from flask import render_template, redirect, request, url_for, flash, session
from app import app
from app.models.application import Application
from app.models.user import User
from app.models.list import List
from app.models.item import ListItems

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
    """"
    Route to enable the user to create/add lists
    """

    # if request.form['title'] and request.form['description']:
    #     title = request.form['title']
    #     description = request.form['description']
    #     return title, description
    # return "no input"

    user = app_class.get_user(session['email'])
    if not user:
        flash('You need to login first')
        return redirect(url_for('login'))
    lists = user.get_lists()
    title = request.form['title']
    description = request.form['description']

    if title and description:
        list_id = app_class.random_id()
        list1 = List(title, description, list_id)
        print(list_id)
        if user.check_valid_list(title):
            if user.create_list(list1):
                flash('List successfully created')
                return redirect(url_for('shopping_list'))
            flash("List title already exists. Try again")
        flash('Invalid title. Only numbers and letters accepted')
        return render_template('shopping_list.html', lists=lists, user=user)

    else:
        flash('You did not input a title or description. Try Again')
        return render_template('shopping_list.html', lists=lists, user=user)


@app.route('/edit/list/<list_id>', methods=['POST', 'GET'])
def edit_list(list_id):
    """"
    This route enables the user to check if they have any lists
     The user can then edit the title  of their list
     :param list_id
    """
    user = app_class.get_user(session['email'])
    if not user:
        return redirect(url_for('login'))

    list = user.get_list(list_id)
    if not list:
        flash('list does not exist')
        return redirect(url_for('shopping_list'))

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        if title and description:
            if user.check_valid_list(title):
                if user.edit_list(list_id, title, description):
                    flash('List successfully edited')
                    return redirect(url_for('shopping_list'))
                flash('List not edited.')
            flash('Invalid title. Only numbers and letters accepted')
            return render_template('edit_list.html', user=user, list=list)

        else:
            flash(" Please provide list title or description")
            return render_template('edit_list.html', user=user, list=list)

    return render_template('edit_list.html', user=user, list=list)


@app.route('/delete/list/<list_id>', methods=['GET', 'POST'])
def delete_list(list_id):
    """"
    This route enables the user to delete an existing list and all items items
    :param list_id
    """
    error = None
    user = app_class.get_user(session['email'])
    if not user:
        return redirect(url_for('login'))
    list1 = user.get_list(list_id)
    if not list1:
        return redirect(url_for('shopping_list'))

    if request.method == 'POST':
        if user.del_list(list_id):
            flash("You have successfully deleted a list")
            return redirect(url_for('delete_list', list_id=list1.list_id))
        error = "Could not delete the Bucket"
    return render_template('delete_list.html', error=error, list=list1, user=user)


@app.route('/view/list/item/<list_id>', methods=['POST', 'GET'])
def items(list_id):
    """"
    This route enables the users to create and view list items for specific lists
    if no items have been created, some text is displayed
    :param list_id
    """
    # error = None
    user = app_class.get_user(session['email'])
    if not user:
        return redirect(url_for('login'))

    list1 = user.get_list(list_id)
    if not list1:
        return redirect(url_for('shopping_list'))

    return render_template('items.html', user=user, list1=list1)


@app.route('/add/list/item/<list_id>', methods=['POST'])
def add_item(list_id):
    """"
        Route to enable the user to create/add bucket lists
        :param list_id
    """
    user = app_class.get_user(session['email'])
    list1 = user.get_list(list_id)
    title = request.form['title']
    quantity = request.form['quantity']
    price = request.form['price']
    status = request.form['status']

    if title and quantity and price and status:
        item_id = app_class.random_id()
        new_item = ListItems(title, quantity, item_id, price, status)
        if status == 'Done':
            list1.get_done_status(new_item)
            flash('You have completed one item')
        else:
            list1.get_undone_status(new_item)
        if list1.check_valid_items(title):
            if list1.create_list_items(new_item):
                flash('Item successfully created')
                return redirect(url_for('items', list_id=list1.list_id))
            flash("Item already exists. Try again")
        flash('Invalid item. Only numbers and letters accepted')
        return render_template('items.html', user=user, list1=list1)

    else:
        flash('You did not input a title or description. Try Again')
        return render_template('items.html', user=user, list1=list1)


@app.route('/edit/list/item/<list_id>/<item_id>', methods=['GET', 'POST'])
def edit_item(list_id, item_id):
    """"
    This route enables the user to edit a single item
    The user is able to edit the item title and description
    :param list_id
    :param item_id
    """
    user = app_class.get_user(session['email'])
    if not user:
        return redirect(url_for('login'))

    list1 = user.get_list(list_id)
    item = list1.get_item(item_id)
    if not list1 and not item:
        flash('Item does not exist')
        return redirect(url_for('items', list_id=list_id))

    if request.method == 'POST':
        title = request.form['title']
        quantity = request.form['quantity']
        price = request.form['price']
        status = request.form['status']

        if title and quantity and price and status:
            item_id = app_class.random_id()
            new_item = ListItems(title, quantity, item_id, price, status)
            if status == 'Done':
                list1.get_done_status(new_item)
                flash('You have completed one item')
            else:
                list1.get_undone_status(new_item)
            if list1.check_valid_items(item):
                if list1.edit_list_item(title, quantity, item_id, price, status):
                    flash('Item successfully edited')
                    return redirect(url_for('items', list_id=list_id))
                flash('Item not edited. Try again')
            flash('Invalid item. Only numbers and letters accepted')
            return redirect(url_for('edit_item', list_id=list_id, item_id=item_id))

        else:
            flash('You did not input a title or description. Try Again')
    return render_template('edit_items.html', user=user, list1=list1, item=item)


@app.route('/delete/list/item/<list_id>/<item_id>', methods=['GET', 'POST'])
def delete_item(list_id, item_id):
    """"
    This route enables the user to delete any of the items
    :param list_id
    :param item_id
    """
    error = None
    user = app_class.get_user(session['email'])
    if not user:
        return redirect(url_for('login'))

    list1 = user.get_list(list_id)
    item = list1.get_item(item_id)
    if not list1 and not item:
        flash('Item does not exist')
        return redirect(url_for('items', list_id=list_id))

    if request.method == 'POST':
        if list1.del_item(item_id):
            flash('Item has been deleted')
            return redirect(url_for('items', list_id=list1.list_id))

        error = 'Item was not deleted'
    return render_template('delete_items.html', error=error, user=user, list1=list1, item=item)


@app.route('/logout')
def logout():
    """"
    route to log out user
    """
    session.pop('email', None)
    flash('You have been logged out')
    return redirect(url_for('login'))
