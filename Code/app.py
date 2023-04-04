from flask import Flask, render_template, request, redirect, url_for, flash
import os
from db_manager import DBHandler

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
def home():
    return 'This is the home page'


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/request_example', methods=['POST', 'GET'])
@login_required
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
        username = request.form.get['username']
        password = request.form.get['password']
        #db = DBHandler()
        if db.login(username, password):
            #token = create_token(username, 60)
            session['token'] = token
            return redirect(url_for('index'))
        else:
            flash('Wrong username or password')
            return redirect(url_for('login'))

@app.route("/signup", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # process form data here
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        # do something with the form data, e.g. store it in a database
        return 'Registration successful!'

    return render_template('signup.html')

@app.route('/users')
def users():
    #print(f"db: {db}")
    users = db.get_users()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run()
