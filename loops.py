# More complex templates using loops

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/loops')
def index():
    dict = {'phy':50, 'che':60, 'maths':70}
    return render_template('loops.html', result = dict)

if __name__ == '__main__':
    app.run(debug = True)
