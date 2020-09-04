import urllib.parse as urlparse
from urllib.parse import urlencode
import requests
import vision
import api

this_dict = {"india": "in", "US": "us", "china": "cn", "japan": "jp"}

# Here you have enter your API key
apikey = api.NEWS_API


def news(query):
    idx = query.split().index('news')
    query = query.split()[idx + 1:]
    params = None
    if len(query) < 3:
        if 'country' in query[0]:
            if query[1] in this_dict:
                params = {'country': this_dict[query[1]], 'apiKey': apikey}

        else:
            params = {'category': query[1], 'apiKey': apikey}

    else:
        if 'country' in query[0]:
            params = {'country': this_dict[query[1]],
                      'category': query[3],
                      'apiKey': apikey}

    url = "https://newsapi.org/v2/top-headlines?"

    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)

    url_parts[4] = urlencode(query)
    response = requests.get(urlparse.urlunparse(url_parts)).json()

    for new in response["articles"]:
        print(str(new['title']))
        vision.speak(new['title'])
