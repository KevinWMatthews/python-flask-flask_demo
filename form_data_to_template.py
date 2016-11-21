from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def get_me_some_data():
    return render-template('get_me_some_data.html')

@app.route('/result', methods = ['POST', 'GET'])
def show_me_some_data():
    if request.method == 'POST':
        result = request.form
        return render_template('show_me_some_data.html', result = result)

if __name__ == '__main__':
    app.run(debug = True)
