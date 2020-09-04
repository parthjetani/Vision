# About Vision 🧠
Vision is a voice assistant service in [Python 3.5+](https://www.python.org/downloads/release/python-360/)
It can understand human speech, talk to user and execute basic commands.

#### Assistant Skills 
*   **Opens a web page** (e.g 'Vision open youtube')
*   **Play videos in Youtube** (e.g 'Vision youtube mozart')
*   **Opens windows office applications (word, powerpoint, excel)** (e.g 'Vision open word')
*   **Tells about something**, by searching on the internet (e.g 'Vision tells me about oranges')
*   **Tells the weather** for a place (e.g 'Vision tell me the weather in Surat')
*   **Tells the current time and/or date** (e.g 'Vision tells me time or date')
*   **Tells the internet speed (ping, uplink and downling)** (e.g 'Vision tell me the internet speed')
*   **Tells the internet availability** (e.g 'Vision is the internet connection ok?')
*   **Tells the daily news** (e.g 'Vision tell me today news')
*   **Opens applications** (e.g 'Vision open firefox')
*   **Tells the current location** (e.g 'Vision tell me current location')
*   **Do basic calculations** (e.g 'Vision calculate (5 + 6) * 8' or 'Vision one plus one')
*   **Send Mail** (e.g 'Vision send mail')
*   **Tell Windows System Information** (e.g 'show me a system information')
*   **Close running applications** (e.g 'Vision close Firefox')
*   **Shutdown/restart your system** (e.g 'Vision shutdown system or Vision restart system')

## Getting Started
### Create KEYs for third party APIs
Vision assistant uses third party APIs for speech recognition,web information search, weather forecasting etc.
All the following APIs have free no-commercial API calls. Subscribe to the following APIs in order to take FREE access KEYs.
*   [OpenWeatherMap](https://openweathermap.org/appid): API for weather forecast.
*   [WolframAlpha](https://developer.wolframalpha.com/portal/myapps/): API for answer questions.
*   [IPINFO](https://ipinfo.io/signup): API for current location.
*   [NEWS](https://newsapi.org/register): API for news.

### Setup Vision in Windows system
*   Download the Vision repo localy:

```bash
git clone https://github.com/parthjetani/Vision
```

*   Put the Keys in settings

**NOTE:** *For better exprerience, before you start the application you can put the free KEYs in the api.py*

```bash
vision\api.py
```

### Start voice assistant

*   Start the assistant service:
```bash
run vision.py
```
