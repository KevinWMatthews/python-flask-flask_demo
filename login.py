# To run this:
#   start your server (python login.py)
#   open the corresponding html in a browser (login.html).
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'Welcome, %s!' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        # To get here, change the form method to 'post' in the html.
        print "This is a HTTP POST"
        user = request.form['user_name']
        return redirect(url_for('success', name = user))
    else:
        # To get here, change the form method to 'get' in the html.
        print "This is a HTTP GET"
        user = request.args.get('user_name')
        return redirect(url_for('success', name = user))

if __name__ == '__main__':
    app.run(debug = True)

'''
For HTML POST,
data is sent in the body of the message (see Form Data in Chrome's Developer Tools)
Request Method:POST
Request URL:http://localhost:5000/login
Python can read data from the message body using request.form()

For HTML GET,
data is appended to the request URL as parameters:
Request Method:GET
Request URL:http://localhost:5000/login?user_name=bill
The parameter list begins with '?' and is '&' delimited.
Python can parse the argument list using request.args.get()
'''
