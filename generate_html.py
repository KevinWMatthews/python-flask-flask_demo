# Generating html dynamically using templates

from flask import Flask, render_template
app = Flask(__name__)

# We can directly return html.
@app.route('/ugly')
def ugly():
    return '<html><body><h1>Hello World!</h1></body></html>'

# Rather than hard-coding all of our html, we can genearte html dynamically
# by using render_template() from the Jinja2 template engine.
@app.route('/')
def index():
    # render_template(template_name, **content)
    return render_template('hello.html', name = 'World')

@app.route('/hello_<user>')
def hello(user):
    return render_template('hello.html', name = user)

if __name__ == '__main__':
    app.run(debug = True)
