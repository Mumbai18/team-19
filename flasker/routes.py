from flask import render_template, flash, redirect, url_for, request, session
from flasker import app, db
from flask_login import current_user, login_user, logout_user, login_required
from flasker.forms import LoginForm
from flasker.models import Student, Applicant, Committee, Donor, Educon

@app.route('/base', methods=['GET', 'POST'])
def base():
    return render_template("base.html")

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
    if str(request.form['category']) == 'student':
        user = Student.query.filter_by(username=request.form['username']).first()
        if user and str(user.password) == str(request.form['password']):
            session['username'] = user.username
            return redirect(url_for('student'))
    elif str(request.form['category']) == 'donor':
        user = Donor.query.filter_by(username=request.form['username']).first()
        if user and str(user.password) == str(request.form['password']):
            session['username'] = user.username
            return redirect(url_for('donor'))
    elif str(request.form['category']) == 'educon':
        user = Educon.query.filter_by(username=request.form['username']).first()
        if user and str(user.password) == str(request.form['password']):
            return redirect(url_for('educon'))
    elif str(request.form['category']) == 'committee':
        user = Committee.query.filter_by(username=request.form['username']).first()
        if user and str(user.password) == str(request.form['password']):
            return redirect(url_for('commmittee'))
    elif str(request.form['category']) == 'applicant':
        user = Applicant.query.filter_by(username=request.form['username']).first()
        if user and str(user.password) == str(request.form['password']):
            return redirect(url_for('applicant'))
    return redirect(url_for('register'))
    # db.session.add(User(username=request.form['username'], password=request.form['password']))
    # db.session.commit()


@app.route('/applicant', methods=['GET', 'POST'])
def applicant():
    return render_template("applicant.html")


@app.route('/committee', methods=['GET', 'POST'])
def committee():
    return render_template("committee.html")

@app.route('/educon', methods=['GET', 'POST'])
def educon():
    return render_template("educon.html")

@app.route('/student')
def student():
    return render_template("student.html")

@app.route('/donor', methods=['GET', 'POST'])
def donor():
    return render_template("donor.html")
