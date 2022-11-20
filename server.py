from flask import Flask, redirect, render_template
from weather import weather_by_city
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('Пользователь', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('login.html', title='Получить доступ', form=form)


@app.route('/')
def login_():
    return redirect('/login')


# @app.route('/success')
# def success():
#     return render_template('index.html')


@app.route('/index')
def index():
    page_title = 'Прогноз погоды'
    weather = weather_by_city('Moscow,Russia')
    if weather:
        weather_txt = 'В Москве {}, {}. Ощущается как {}'.format(*weather)
    else:
        weather_txt = 'Сервер погоды временно недоступен'
    return render_template('index.html', page_title=page_title, weather_text=weather_txt)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    # app.run(debug=True)
