from datetime import datetime

from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder="static")


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/holidays')
def holidays():
    with open('holidays.txt') as f:
        h = f.readlines()
    return jsonify([x.strip() for x in h])


if __name__ == "__main__":
    app.run(debug=True)
