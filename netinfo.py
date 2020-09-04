import requests
import speedtest
import vision


def Speed():
    st = speedtest.Speedtest()
    vision.speak("What speed do you want to test?")
    txt = vision.command()
    if 'download' in txt:
        vision.speak("Checking download speed...")
        vision.speak("your download speed is %d Mbps" % (st.download() / (10 ** 6)))
    elif 'upload' in txt:
        vision.speak("Checking upload speed...")
        vision.speak("your upload speed is %d Mbps" % (st.upload() / (10 ** 6)))
    elif 'ping' in txt:
        server_name = []
        st.get_servers(server_name)
        vision.speak("%d ms" % st.results.ping)
    return


def ConnectionCheck():
    try:
        requests.get(url="http://www.google.com", timeout=3)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False


def InternetConnection():
    vision.speak("Checking internet connection...")
    if ConnectionCheck():
        vision.speak("You are connected to internet...")
    else:
        vision.speak("You are not connected to internet...")
        vision.speak("Please connect first...")
    return
