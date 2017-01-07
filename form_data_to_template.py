from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def get_me_some_data():
    return render_template('get_me_some_data.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        # This gets the results of the request as a dictionary object.
        result = request.form
        # We pass the dictionary object to the html template, which parses and uses it.
        return render_template('result.html', result = result)

if __name__ == '__main__':
    app.run(debug = True)
