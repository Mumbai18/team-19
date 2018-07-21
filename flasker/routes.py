from flask import render_template, flash, redirect, url_for, request
from flasker import app, db
from flask_login import current_user, login_user, logout_user, login_required
from flasker.forms import LoginForm
from flasker.models import User

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    # form = RegisterForm()

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # form = LoginForm()
    # passed = 0
    # if form.validate_on_submit():
    #     flash('Login requested for user {}, remember_me={}'.format(
    #         form.username.data, form.remember_me.data))
    #     passed = 1
    #     return redirect(url_for('index', passed))
    return render_template('login.html', title='Sign In')

@app.route('/log', methods=['POST'])
def log():
    # print(request.form['username'])

    user = User.query.filter_by(username=request.form['username']).first()
    if user and str(user.password)==str(request.form['password']):
        if str(request.form['category']) == 'student':
            return redirect(url_for('student'))
        elif str(request.form['category']) == 'donor':
            return redirect(url_for('donor'))
        elif str(request.form['category']) == 'educon':
            return redirect(url_for('educon'))
        elif str(request.form['category']) == 'committee':
            return redirect(url_for('commmittee'))
        elif str(request.form['category']) == 'applicant':
            return redirect(url_for('applicant'))
    return redirect(url_for('register'))
    # db.session.add(User(username=request.form['username'], password=request.form['password']))
    # db.session.commit()

@app.route('/applicant', methods=['GET', 'POST'])
def applicant():
    if

@aa

