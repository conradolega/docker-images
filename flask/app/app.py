from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def root():
    return jsonify({})


@app.route('/ping')
def ping():
    return jsonify(result='pong')


app.run(host='0.0.0.0')
