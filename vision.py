import warnings
import pyttsx3
import speech_recognition as sr
import datetime
import random
import skill
import netinfo

# adding entry into the specifications
# of the warnings filter.
warnings.filterwarnings('ignore')

# Create a engine, set voice property and rate of voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

# This is the list of wake, closing and compos
ready = ['vision', 'you there vision', 'are you there vision', 'vision are you there', 'vision you there',
         'are you ready', 'vision are you ready', 'you ready vision', 'vision you ready']
closing = ['terminate', 'terminate now', 'exit', 'exit now', 'close', 'bye', 'ok bye', 'ok close', 'close conversation',
           'close yourself', 'end now', 'end', 'end conversation']
compos = ['At your service', 'Ask me', 'Waiting for your command', 'Tell me something to do', 'How can I help you?']


# Create a speak function
def speak(audio):
    print("Vision: " + audio)
    engine.say(audio)
    engine.runAndWait()


# Create a command function that will convert voice command to text command
def command():
    cmd = sr.Recognizer()
    with sr.Microphone() as source:
        cmd.adjust_for_ambient_noise(source, duration=1)
        print('Say something...')
        cmd.pause_threshold = 1
        audio = cmd.listen(source)
        try:
            txt = cmd.recognize_google(audio, language='en-IN').lower()
            print('You said: ' + txt + '\n')
        except sr.UnknownValueError:
            txt = command()
            print('You said: ' + txt + '\n')
        except sr.RequestError as e:
            print("Request Failed; {0}".format(e))
    return txt


# Create a greeting function
def greeting():
    currentH = int(datetime.datetime.now().hour)
    if 0 <= currentH < 12:
        speak('Good Morning Sir...')
    if 12 <= currentH < 17:
        speak('Good Afternoon Sir...')
    if currentH >= 17 and currentH != 0:
        speak('Good Evening Sir...')


def split(x):
    txt = x.split(" ")
    return txt[0]


# Driver Code
if __name__ == "__main__":
    while True:
        if netinfo.ConnectionCheck():
            query = command()
            if query in ready:
                greeting()

                speak(random.choice(compos))
                while True:
                    query = command()

                    if query == 0:
                        continue

                    if query in closing:
                        speak("Ok bye....")
                        speak("have a nice day...")
                        break

                    skill.AssistantSkill(query)
            else:
                speak("Speak proper words So that I can ready for your help")
        else:
            speak("Your Wi-Fi is turned off, so I can't help you with that at the moment.")
            speak("Turn on Wi-Fi and try again...")
