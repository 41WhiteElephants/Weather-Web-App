from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['POST', 'GET'])
def send():
    if request.method == 'POST':
        coordinates = request.form['data']
        return render_template('result.html', coordinates=coordinates)


if __name__ == '__main__':
    app.run(debug=True)
