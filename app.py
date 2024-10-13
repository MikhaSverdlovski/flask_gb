import datetime

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Length, NumberRange

app = Flask(__name__)


class registerForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=3, max=20)])
    age = IntegerField(validators=[InputRequired(), NumberRange(min=0, max=100)])


@app.route('/register', methods=['POST'])
def register():
    form = registerForm()
    if form.validate_on_submit():
        username = form.username.data
        age = form.age.data
        return f'<h1>Hello {username} {age}!</h1>'
    else:
        return f'<h1>Invalid username or age</h1><br> {form.errors}', 400

@app.route('/uptime', methods=['GET'])
def uptime():
    uptime = datetime.datetime.now()
    return str(uptime)


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
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True, port=8000)
