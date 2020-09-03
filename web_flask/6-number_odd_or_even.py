#!/usr/bin/python3
""" flask app """

from flask import Flask

app = Flask('__name__')


@app.route('/'. strict_slashes=False)
def hello_hbnb():
    ''' Display 'Hello HBNB!' '''
    return 'Hello HBNB!'


@app.route('/hbnb'. strict_slashes=False)
def dpl_hbnb():
    ''' Display 'HBNB' '''
    return 'HBNB'


@app.route('/c/<text>'. strict_slashes=False)
def dpl_ctext(text):
    ''' Display 'C <text>' '''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/'. strict_slashes=False)
@app.route('/python/<text>'. strict_slashes=False)
def dpl_ptext(text="is cool"):
    ''' Display 'C <text>' '''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>'. strict_slashes=False)
def dpl_number(n):
    ''' Display '<n> is a number' '''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>'. strict_slashes=False)
def dpl_ntemplate(n):
    ''' Display '<n>' per html template '''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>'. strict_slashes=False)
def dpl_noddeven(n):
    ''' Display '<n>' if odd ot even per html template '''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    ''' main '''
    app.run(host='0.0.0.0', port=5000)
