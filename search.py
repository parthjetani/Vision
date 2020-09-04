import webbrowser
import urllib.request
import urllib.parse
import re
import time
import vision


def search_web(cmd):
    if 'youtube' in cmd:
        vision.speak("Opening in youtube")
        idx = cmd.split().index('youtube')
        txt = cmd.split()[idx + 1:]
        search_keyword = urllib.parse.urlencode({'search_query': txt})
        html = urllib.request.urlopen("https://www.youtube.com/results?" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        webbrowser.open("https://www.youtube.com/watch?v=" + video_ids[0])
        time.sleep(5)
        return

    elif 'wikipedia' in cmd:

        vision.speak("Opening Wikipedia")
        idx = cmd.split().index('wikipedia')
        txt = cmd.split()[idx + 1:]
        webbrowser.open("https://en.wikipedia.org/wiki/" + '_'.join(txt))
        time.sleep(5)
        return

    else:

        if 'google' in cmd:
            vision.speak("Searching on Google")
            idx = cmd.split().index('google')
            txt = cmd.split()[idx + 1:]
            webbrowser.open("https://www.google.com/search?q=" + '+'.join(txt))
            time.sleep(5)

        elif 'search' in cmd:
            vision.speak("Searching on Google")
            idx = cmd.split().index('search')
            txt = cmd.split()[idx + 1:]
            webbrowser.open("https://www.google.com/search?q=" + '+'.join(txt))
            time.sleep(5)

        else:
            vision.speak("Searching on Google")
            webbrowser.open("https://www.google.com/search?q=" + '+'.join(cmd.split()))
            time.sleep(5)
