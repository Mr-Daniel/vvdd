import json

from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder="static")


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/holidays')
def holidays():
    with open('holidays_2021.txt') as f:
        h = f.readlines()
        h = ["{},base".format(x) for x in h]
    with open('holidays_daniel_2021.txt') as f:
        h1 = f.readlines()
        h.extend(h1)
    return jsonify([x.strip().replace('\n', '') for x in h])


@app.route('/addholiday/<hdate>/<time_period>')
def add_holiday(hdate, time_period):
    with open('holidays_daniel_2021.txt', 'a') as f:
        f.write("{},{}\n".format(hdate, time_period))
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=55555)
