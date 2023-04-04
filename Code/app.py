from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
from db_manager import DBHandler
from token_management import create_token, check_token

app = Flask(__name__)
secret_key = os.urandom(32)
app.secret_key = secret_key

db = DBHandler("sqlite:///Code/social_media.sqlite")

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
@login_required
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
            token = create_token(username, 60)
            session['token'] = token
            print(token)
            print("Login successful")
            return render_template('dashboard.html', username=username)
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

if __name__ == '__main__':
    app.run()
