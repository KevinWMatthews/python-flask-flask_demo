# Read js and css from /static.

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('js_and_css.html')

if __name__ == '__main__':
    app.run(debug = True)
