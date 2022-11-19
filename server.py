from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

# http://api.worldweatheronline.com/premium/v1/weather.ashx?key=5d20b324861d406ab66183759221911&q=Moscow,Russia&format=json&num_of_days=1&lang=ru
@app.route('/')
def index():
    weather = weather_by_city('Moscow,Russia')
    if weather:
        return 'В Москве {}, {}. Ощущается как {}'.format(*weather)
    else:
        return 'Сервер погоды временно недоступен'


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
