from flask import Flask, render_template
from weather import weather_by_city

app = Flask(__name__)

# http://api.worldweatheronline.com/premium/v1/weather.ashx?key=5d20b324861d406ab66183759221911&q=Moscow,Russia&format=json&num_of_days=1&lang=ru
@app.route('/')
def index():
    page_title = 'Прогноз погоды'
    weather = weather_by_city('Moscow,Russia')
    if weather:
        weather_txt = 'В Москве {}, {}. Ощущается как {}'.format(*weather)
    else:
        weather_txt = 'Сервер погоды временно недоступен'
    # return f'''
    # <html>
    #     <title>Прогноз погоды</title>
    #     <body><h1>{weather_txt}</h1></body>
    # </html>
    # '''
    return render_template('index.html', page_title=page_title, weather_text=weather_txt)


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
