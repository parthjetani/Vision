import requests
import vision
import api

# Here You have to enter your ipinfo token number
token_number = API.IPSTACK_API


def location():
    try:
        res = requests.get('https://ipinfo.io?token=' + token_number)
        data = res.json()
        country = data['country']
        loc = data['loc'].split(',')

        if 'IN' in country:
            country = 'India'

        vision.speak("Your latitude: {} , longitude: {}".format(loc[0], loc[1]))
        vision.speak("You are currently in {}, {}, {}".format(data['city'], data['region'], country))
        vision.speak("Your timezone is {}".format(data['timezone']))

    except ConnectionError as e:
        vision.speak("Unable to get current location with error message: {0}".format(e))
    return
