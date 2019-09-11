#Flask Modules
import config
from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
import base64
import os.path
from os import path

app = Flask(__name__)

app.secret_key = '\xb7\x90M\xd962\x80}\x1e\xb8'

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You must login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/hello')
@login_required
def home():
    #return "Hello, World!"  # return a string
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if path.exists("/etc/secrets/username"):
        f = open("/etc/secrets/username", "r")
        ruser = f.read()
    else:
        print(" Kube secrets not set use default to login")
        ruser = "admin"

    if path.exists("/etc/secrets/password"):
        q = open("/etc/secrets/password", "r")
        rpasswd = q.read()
    else:
        print(" Kube secrets not set use default for password")
        rpasswd = "password"
        
    if request.method == 'POST':
        #if request.form['username'] != ruser.decode('base64') or request.form['password'] != rpasswd.decode('base64'):
        if request.form['username'] != ruser or request.form['password'] != rpasswd:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
