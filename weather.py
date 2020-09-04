import requests
import vision
import api

city = ['surat', 'bhavnagar', 'Ahmedabad', 'Vadodara', 'Rajkot', 'Delhi', 'Mumbai', 'Bangalore', 'Hyderabad',
        'Chennai', 'Kolkata']

# Here You have enter your API key
apikey = api.WOLFRAMALPHA_API


def weather_data(query):
    res = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?' + query + '&appid=' + apikey + '&units=metric')
    return res.json()


def print_weather(result, cty):
    vision.speak("{}'s temperature: {}°C ".format(cty, result['main']['temp']))
    vision.speak("Wind speed: {} meter per second".format(result['wind']['speed']))
    vision.speak("Description: {}".format(result['weather'][0]['description']))
    vision.speak("Weather: {}".format(result['weather'][0]['main']))
    vision.speak("Visibility:{} kilometer".format(result['visibility'] / 1000))


def main(txt):

    try:
        txt = txt.split()
        for i in range(len(city)):
            if city[i] in txt:
                query = 'q=' + city[i]
                w_data = weather_data(query)
                print_weather(w_data, city[i])
    except ArithmeticError:
        vision.speak('City name not found...')
