import pyttsx3
import speech_recognition as sr
import wolframalpha
import warnings
import datetime
import os

# Ignore any warning messages
warnings.filterwarnings('ignore')

# Create a engine, set voice property and rate of voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # voices[1] for Female and voices[0] for male
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

# This is a wake and closing list
WAKE = ["hello", "hi", "hello vision", "hi vision", "hey", "hay", 'hey vision', 'hei']
CLOSING = ['terminate', 'terminate now', 'exit', 'exit now', 'close', 'bye', 'ok bye', 'ok close'
           'close conversation', 'close yourself', 'end now', 'end', 'end conversation']


# Create a command function that will convert voice command to text command
def command():
    cmd = sr.Recognizer()
    with sr.Microphone() as source:
        cmd.adjust_for_ambient_noise(source, duration=1)
        print('Say something...')
        cmd.pause_threshold = 1
        audio = cmd.listen(source)
        try:
            query = cmd.recognize_google(audio, language='en-in').lower()
            print('You said: ' + query + '\n')
        # loop back to continue to listen for commands if unrecognizable speech is received
        except sr.UnknownValueError:
            query = command()
        except sr.RequestError as e:
            # If any error in request results from Google Speech Recognition service
            print("Request Failed; {0}".format(e))
    return query


# Create a speak function
def speak(audio):
    print("Vision: " + audio)
    engine.say(audio)
    engine.runAndWait()


# Create a greeting function
def greeting():
    currentH = int(datetime.datetime.now().hour)
    if 0 <= currentH < 12:
        speak('Good Morning Sir...')
    if 12 <= currentH < 17:
        speak('Good Afternoon Sir...')
    if currentH >= 17 and currentH != 0:
        speak('Good Evening Sir...')


# function used to open application
# present inside the system.
def open_application(query):
    if "chrome" in query:
        speak("Google Chrome")
        os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
        return

    elif "firefox" in query or "mozilla" in query:
        speak("Opening Mozilla Firefox")
        os.startfile('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
        return

    elif "word" in query:
        speak("Opening Microsoft Word")
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk')
        return

    elif "excel" in query:
        speak("Opening Microsoft Excel")
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk')
        return

    else:
        speak("Application not available")
        return


# This a process function
# Which will give output according to user input
def process_text(query):
    try:
        if "who are you" in query or "define yourself" in query:
            speaks = '''Hello, I am Person. Your personal Assistant. I am here to make your life easier. You can 
            command me to perform various tasks such as calculating sums or opening applications etcetra '''
            speak(speaks)
            return

        elif "who made you" in query or "created you" in query:
            speaks = "I have been created by Parth Jetani."
            speak(speaks)
            return

        elif "calculate" in query.lower():
            # write your wolframalpha app_id here
            app_id = "P74U42-8AJQ6U6X9K"
            client = wolframalpha.Client(app_id)

            indx = query.split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            speak("The answer is " + answer)
            return

        elif 'open' in query:
            # another function to open
            # different application availaible
            open_application(query)
            return

    except EOFError:
        speak("I can't understand your command please give valid command...")
        query = command()
        return query


# Driver Code
if __name__ == "__main__":
    query = command()

    if query in WAKE:

        greeting()
        speak("What can i do for you sir?...")

        while True:

            query = command()

            if query == 0:
                continue

            if query in CLOSING:
                speak("Ok bye...Sir....")
                speak("have a nice day sir...")
                break

            # calling process text to process the query
            process_text(query)
