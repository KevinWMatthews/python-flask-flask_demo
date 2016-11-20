# https://www.tutorialspoint.com/flask
from flask import Flask, redirect, url_for
app = Flask(__name__)

# Browse to this URL to view the page defined by the hello_world() function.
# We're using the decorator '@' to bind the two.
@app.route('/')
@app.route('/index')
def index():
    return 'Welcome to my webpage! Browse to /hello, /goodbye, /hello_NAME, or /goodbye_NAME'

@app.route('/admin')
def hello_admin():
    return 'Welcome to Admin Land!'

@app.route('/hello')
def hello_world():
    return 'Hello, world of Flask!'

@app.route('/hello_<user>')
def hello_user(user):
    if user == 'admin':
        return redirect(url_for('hello_admin')) # Pass the function name, not the URL (hence url_FOR).
    else:
        return 'Hello, %s!' % (user)

# This is equivalent to the route decorator.
def goodbye_world():
    return 'Goodbye, world.'
app.add_url_rule('/goodbye', 'goodbye', goodbye_world)

@app.route('/goodbye_<user>')
def goodbye_user(user):
    return 'Goodbye, %s.' % (user)

if __name__ == '__main__':
    # Before running this app, install Flask.
    # Then run it using python hello.py
    #
    # If run in debug mode, the server will reload itself every time the code changes.
    app.run(debug = True)
    # app.run
