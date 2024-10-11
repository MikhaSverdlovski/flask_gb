import datetime

from flask import Flask



app = Flask(__name__)


@app.route('/')
def test_func(username=None):
    return f'Hello <b>World</b>'


@app.route('/even/<int:number>')
def even_func(number):
    if number % 2 == 0:
        return f'{number} is <b>even</b>'
    else:
        return f'{number} is odd'


@app.route('/time')
def time_func():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    app.run(debug=True, port=8000)


