import vision
import location
import mediaplayer
import systeminfo
import netinfo
import wolframalph
import mail
import news
import desktopapps
import search
import weather
import date_time
import os

# This are the same list
media_toggle = [['play music', 'play media', 'play some music'], ['play video', 'play movie']]
system_toggle = ["show me a system information", 'system information', "show me a full system information"]
web_dict = ["search", "youtube", "google", "wikipedia"]
frequent = [['what is the time right now', "what's the time right now", 'what time is it right now', "what's the time",
             'what time is it in the clock', 'what is the time', "what's the time now", 'what time is it now',
             'tell me the time'],
            ["what's the date today", 'what is the date today', "today's date is", "tell me today's date",
             "today's date is",
             "what is today's day", 'what is the day today', "today's day is",
             "tell me today's day"]]
weatherRep = ['how is the weather today', 'current weather conditions', 'how is the weather', 'weather conditions',
              'weather forecast']
whereAbouts = ['where am I', 'what is my location', 'what is my current location', "what's my location",
               "what's my current location", 'get my location', 'what is this place']


# This a skill function
# Which will give output according to user input
def AssistantSkill(cmd):
    try:
        if vision.split(cmd) in web_dict:
            search.search_web(cmd)
            return

        elif cmd in media_toggle[0]:
            vision.speak("opening your music player")
            mediaplayer.music()
            return

        elif cmd in media_toggle[1]:
            vision.speak("opening your video player")
            mediaplayer.video()
            return

        elif 'send email' in cmd or 'sent mail' in cmd:
            mail.mail()
            return

        elif "who are you" in cmd or "define yourself" in cmd:
            speaks = '''Hello, I am Person. Your personal Assistant. I am here to make your life easier. You can 
            command me to perform various tasks such as calculating sums or opening applications etc '''
            vision.speak(speaks)
            return

        elif "who made you" in cmd or "created you" in cmd:
            speaks = "I have been created by Developer."
            vision.speak(speaks)
            return

        elif "calculate" in cmd.lower():
            wolframalph.WolframSkills(cmd)
            return

        elif cmd in frequent[1]:
            date_time.tell_the_date()
            return

        elif cmd in frequent[0]:
            date_time.tell_the_time()
            return

        elif cmd in system_toggle:
            systeminfo.SystemInfo()
            return

        elif 'network speed' in cmd:
            netinfo.Speed()
            return

        elif 'check internet connection' in cmd:
            netinfo.InternetConnection()
            return

        elif 'open' in cmd:
            desktopapps.open_application(cmd)
            return

        elif 'close' in cmd:
            desktopapps.close_application(cmd)
            return

        elif 'news' in cmd:
            news.news(cmd)
            return

        elif "weather" in cmd:
            weather.main(cmd)
            return

        elif cmd in whereAbouts:
            location.location()
            return

        elif "shutdown" in cmd:
            os.system("shutdown /s /t 1")
            return

        elif "restart" in cmd:
            os.system("shutdown /r /t 1")
            return

        else:
            vision.speak("Please check my skill listed in info file...")
            return

    except Exception as e:
        vision.speak(e)
        return
