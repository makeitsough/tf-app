from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)


@app.route('/members')
def members():
    return {'members': ['John', 'Paul', 'George', 'Ringo']}

if __name__ == '__main__':
    app.run(debug=True)