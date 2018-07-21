from flask import render_template, flash, redirect, url_for, request
from flasker import app, db


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')