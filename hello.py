# Before running this app, install Flask.
# Then run it using python hello.py
#
# https://www.tutorialspoint.com/flask
from flask import Flask, redirect, url_for
app = Flask(__name__)

# @route(rule, options)
# Bind the URL given in rule to the function that follows.
#
# Browsing to the given URL calls the method that is bound to it.
# This method populates the web page.
#
# '@' is a decorator that binds the methods.
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
        # redirect(location, ...)
        # location is the url to which the user will be redirected
        #
        # url_for(endpoint, **values)
        # Generate a url a method (endpoint)
        return redirect(url_for('hello_admin')) # Pass the function name, not the URL (hence url_FOR).
    else:
        return 'Hello, %s!' % (user)

# This is equivalent to the route decorator.
# It is not preferred since it is more verbose.
def goodbye_world():
    return 'Goodbye, world.'
app.add_url_rule('/goodbye', 'goodbye', goodbye_world)

@app.route('/goodbye_<user>')
def goodbye_user(user):
    return 'Goodbye, %s.' % (user)

if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # host      defaults to localhost (127.0.0.1)
    # port      defaults to 5000
    # debug     when true, the server will reload itself every time the code changes.
    app.run(debug = True)
    # app.run
