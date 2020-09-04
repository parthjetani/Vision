import wolframalpha
import vision
import netinfo
import api

# Here You have to enter your Wolframalpha API key
WOLFRAMALPHA_API = {'key': api.WOLFRAMALPHA_API}


def WolframSkills(cmd):
    """
    Make a request in wolfram Alpha API and prints the response.
    """
    client = wolframalpha.Client(WOLFRAMALPHA_API['key'])
    try:
        if WOLFRAMALPHA_API['key']:
            vision.speak("Wait a second, I search..")
            res = client.query(cmd)
            wolfram_result = next(res.results).text
            vision.speak(f"The Answer Is {wolfram_result}")
        else:
            vision.speak("WolframAlpha API is not working.\n"
                         "You can get an API key from: https://developer.wolframalpha.com/portal/myapps/ ")

    except Exception as e:
        if netinfo.ConnectionCheck():
            # If there is an error but the internet connect is good, then the Wolfram API has problem
            vision.speak('There is no result from Wolfram API with error: {0}'.format(e))
        else:
            vision.speak('Sorry, but I could not find something')
