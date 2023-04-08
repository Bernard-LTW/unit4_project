from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

from Code import secure_password
from db_manager import DBHandler
from token_management import create_token, check_token, get_username_from_token
from jinja2 import Environment
from secure_password import *

app = Flask(__name__)
app.jinja_env.filters['strfttime'] = datetime.strftime
# app.jinja_env.filters['highlight'] = highlight
# app.jinja_env.filters['PythonLexer'] = PythonLexer
# app.jinja_env.filters['HtmlFormatter'] = HtmlFormatter
env = Environment()
env.filters['strftime'] = datetime.strftime
secret_key = os.urandom(32)
app.secret_key = secret_key

db = DBHandler("sqlite:///Code/social_media.sqlite")
app.static_folder = 'static'
def login_required(f):
    def wrapper(*args, **kwargs):
        if 'token' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrapper

@app.route('/')
def hello_world():  # put application's code here
    try:
        token = session['token']
        username = get_username_from_token(token)
        return redirect(url_for('dashboard'))
    except KeyError:
        return redirect(url_for('login'))


@app.route('/home')
def home():
    return 'This is the home page'


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/request_example', methods=['POST', 'GET'])
def request_example():
    result = ""
    result2 = ""
    if request.method == 'POST':
        # password check
        password = request.form.get("check_pass")
        if password:
            result2 = len(password) >= 8
            result2 = "Password is valid" if result else "Password is invalid"
    elif request.method == 'GET':
        # currency conversion
        hkd_value = request.args.get("hkd_value")
        if hkd_value:
            jpy_value = int(hkd_value) * 17
            result = f"{jpy_value:.2f} JPY"
    return render_template("request_example.html", data=result, data2=result2)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        #db = DBHandler()
        if db.login(username, password):
            token = create_token(username, 120)
            session['token'] = token
            print(token)
            print("Login successful")
            return redirect(url_for('dashboard'))
        else:
            print("Login failed")
            flash(('Wrong username or password',"danger"))
            return redirect(url_for('login'))

@app.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        # process form data here
        username = request.form.get('newUsername')
        password = request.form.get('newPassword')
        confirm_password = request.form.get('confirmPassword')
        if password != confirm_password:
            flash(('Passwords do not match',"danger"))
            return redirect(url_for('register'))
        elif db.check_user(username):
            flash(('Username already exists',"danger"))
            return redirect(url_for('register'))
        else:
            db.create_user(username, password)
            flash(('Registration successful. Please log in now',"success"))

            return redirect(url_for('login'))
        # do something with the form data, e.g. store it in a database
    return render_template('login.html')

@app.route('/users')
def users():
    #print(f"db: {db}")
    users = db.get_users()
    return render_template('users.html', users=users)

@app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect(url_for('login'))

# @app.route("/my_posts")
# def my_posts():
#     try:
#         token = session['token']
#         if check_token(token):
#             username = get_username_from_token(token)
#             user = db.get_user(username)
#             my_posts = db.get_own_posts(username)
#             stats = db.get_user_stats(username)
#             print(my_posts)
#             return render_template('mypost.html', user=user, posts=my_posts, stats=stats)
#         else:
#             return redirect(url_for('login'))
#     except KeyError:
#         return redirect(url_for('login'))

@app.route("/create_post", methods=['POST'])
def create_post():
    if request.method == 'POST':
        # process form data here
        title = request.form.get('title')
        content = request.form.get('content')
        code = request.form.get('code')
        token = session['token']
        username = get_username_from_token(token)
        db.create_post(title, content, code, username)
        flash(('Post created successfully',"success"))
        return redirect(url_for('my_posts'))
    return render_template('mypost.html')


@app.route("/delete_post/<int:post_id>")
def delete_post(post_id):
    db.delete_post(post_id)
    return redirect(url_for('my_posts'))

@app.route("/new_post", methods=['GET', 'POST'])
def new_post():
    try:
        token = session['token']
        if request.method == 'POST':
            # process form data here
                title = request.form.get('title')
                content = request.form.get('content')
                code = request.form.get('code')
                if request.form.get('language') == 'other':
                    language = request.form.get('other-language')
                else:
                    language = request.form.get('language')
                username = get_username_from_token(token)
                db.create_post(title, content, code, language, username)
                flash(('Post created successfully',"success"))
                return redirect(url_for('my_posts'))
        elif request.method == 'GET':
            return render_template('new_post.html')
    except KeyError:
        return redirect(url_for('login'))





@app.route("/dashboard")
def dashboard():
    try:
        token = session['token']
        if check_token(token):
            username = get_username_from_token(token)
            sort_by = request.args.get('sort_by', default='time', type=str)
            print(sort_by)
            posts = db.get_sorted_posts(sort_by)
            return render_template('dashboard.html', title='Dashboard', posts=posts, username=username)
        else:
            return redirect(url_for('login'))
    except KeyError:
        return redirect(url_for('login'))

@app.route("/add_like/<int:post_id>")
def add_like(post_id):
    try:
        token = session['token']
        if check_token(token):
            #username = get_username_from_token(token)
            db.add_like(post_id)
            #return redirect(url_for('dashboard'))
            return redirect(request.referrer)
        else:
            return redirect(url_for('login'))
    except KeyError:
        return redirect(url_for('login'))

@app.route("/add_dislike/<int:post_id>")
def add_dislike(post_id):
    try:
        token = session['token']
        if check_token(token):
            #username = get_username_from_token(token)
            db.remove_like(post_id)
            #return redirect(url_for('dashboard'))
            return redirect(request.referrer)
        else:
            return redirect(url_for('login'))
    except KeyError:
        return redirect(url_for('login'))

@app.route("/profile/<username>")
def profile(username):
    try:
        token = session['token']
        if check_token(token):
            posts = db.get_own_posts(username)
            user = db.get_user(username)
            stats = db.get_user_stats(username)
            return render_template('profile.html', username=username, posts=posts, user=user,stats=stats)
        else:
            return redirect(url_for('login'))
    except KeyError:
        return redirect(url_for('login'))


@app.route("/my_profile", methods=['GET', 'POST'])
def my_profile():
    try:
        token = session['token']
        if check_token(token):
            username = get_username_from_token(token)
            if request.method == 'POST':
                pass
                #process form data here
                #Change either password or username
            elif request.method == 'GET':
                user = db.get_user(username)
                stats = db.get_user_stats(username)
                myposts = db.get_own_posts(username)
                return render_template('my_profile.html', user=user, my_posts=myposts, stats=stats)
        else:
            return redirect(url_for('login'))
    except KeyError:
        return redirect(url_for('login'))


@app.route("/change_password", methods=['POST'])
def change_password():
    current = request.form.get('current_password')
    new = request.form.get('new_password')
    confirm = request.form.get('confirm_password')
    try:
        token = session['token']
        if check_token(token):
            username = get_username_from_token(token)
            if secure_password.check_password(current,db.get_password(username)):
                if new == confirm:
                    db.change_password(username, new)
                    flash(('Password changed successfully.',"success"))
                    return redirect(url_for('my_profile'))
                else:
                    flash(('New passwords do not match',"danger"))
                    return redirect(url_for('my_profile'))
            else:
                flash(('Current password is incorrect',"danger"))
                return redirect(url_for('my_profile'))
        else:
            return redirect(url_for('login'))
    except KeyError:
        return redirect(url_for('login'))


@app.route("/edit_post/<int:post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    try:
        token = session['token']
        if check_token(token):
            username = get_username_from_token(token)
            if request.method == 'POST':
                # process form data here
                title = request.form.get('title')
                content = request.form.get('content')
                code = request.form.get('code')
                if request.form.get('language') == 'other':
                    language = request.form.get('other-language')
                else:
                    language = request.form.get('language')
                db.edit_post(post_id, title, content, code, language)
                flash(('Post edited successfully',"success"))
                return redirect(url_for('my_posts'))
            elif request.method == 'GET':
                post = db.get_post(post_id)
                return render_template('my_profile.html', post=post)
        else:
            return redirect(url_for('login'))
    except KeyError:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(port=80, debug=True)

