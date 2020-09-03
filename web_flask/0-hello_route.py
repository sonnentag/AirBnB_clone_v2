#!/usr/bin/python3
""" flask app """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' hello hbnb'''
    return 'Hello HBNB!'


if __name__ == '__main__':
    ''' main '''
    app.run(host='0.0.0.0', port=5000)
