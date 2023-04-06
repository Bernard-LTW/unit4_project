from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
from db_manager import DBHandler
from token_management import create_token, check_token, get_username_from_token
from jinja2 import Environment
# from pygments.lexers import PythonLexer
# from pygments.formatters import HtmlFormatter
# from pygments import highlight

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
    return render_template('login.html')


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
            return render_template('dashboard.html', username=username, token=token)
        else:
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

@app.route("/my_posts")
def my_posts():
    try:
        token = session['token']
        if check_token(token):
            username = get_username_from_token(token)
            my_posts = db.get_own_posts(username)
            print(my_posts)
            return render_template('mypost.html', username=username, posts=my_posts)
        else:
            return redirect(url_for('login'))
    except KeyError:
        return redirect(url_for('login'))

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
            return render_template('dashboard.html', username=username,token=token)
        else:
            return redirect(url_for('login'))
    except KeyError:
        return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(port=80, debug=True)
