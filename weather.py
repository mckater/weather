import requests


def weather_by_city(city_name):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': '5d20b324861d406ab66183759221911',
        'q': city_name,
        'format': 'json',
        'num_of_days': 1,
        'lang': 'ru'
    }
    try:
        result = requests.get(weather_url, params=params)
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]["temp_C"], \
                           weather['data']['current_condition'][0]["lang_ru"][0]['value'], \
                           weather['data']['current_condition'][0]["FeelsLikeC"]
                except(IndexError, TypeError):
                    return False
        return False
    except(requests.RequestException, ValueError):
        print('Интернет-запрос не удался')
        return False


if __name__ == '__main__':
    print('В Москве {}, {}. Ощущается как {}'.format(*weather_by_city('Moscow,Russia')))
