from flask import Flask, render_template, request, redirect, url_for, flash


# flash(message, category)
#   Pass a message to the next request.
#   The next request is typically a template.
#   The template can extract the message with get_flashed_messages().
#   category:   error
#               info
#               warning

app = Flask(__name__)
# For storing password?
app.secret_key = 'secret key for flashing messages'

@app.route('/')
def index():
    return render_template('flash_index.html')

def verify_login_credentials(username, password):
    if username != 'admin':
        return False
    if password != 'admin':
        return False
    return True

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if verify_login_credentials(username, password):
            flash('Login success')
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password. Please try again.'

    return render_template('flash_login.html', error = error)

if __name__ == "__main__":
    app.run(debug = True)
