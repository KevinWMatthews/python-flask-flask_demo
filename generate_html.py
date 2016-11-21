from flask import Flask, render_template
app = Flask(__name__)

# We can genearte html dynamically by using render_template() from the Jinja2 template engine.
@app.route('/')
def index():
    return render_template('hello.html', name = 'World')

@app.route('/hello_<user>')
def hello(user):
    return render_template('hello.html', name = user)

app.route('/ugly')
def ugly():
    return '<html><body><h1>Hello World!</h1></body></html>'

if __name__ == '__main__':
    app.run(debug = True)
