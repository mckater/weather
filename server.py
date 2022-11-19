from flask import Flask

app = Flask(__name__)

# http://api.worldweatheronline.com/premium/v1/weather.ashx?key=5d20b324861d406ab66183759221911&q=Moscow,Russia&format=json&num_of_days=1&lang=ru
@app.route('/')
def index():
    return 'Hello!'


if __name__ == '__main__':
    app.run()