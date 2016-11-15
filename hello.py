from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world of Flask!'

if __name__ == '__main__':
    # If run in debug mode, the server will reload itself every time the code changes.
    app.run(debug = True)
    # app.run
