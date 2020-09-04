import vision
import os


def open_application(cmd):
    if "word" in cmd:
        vision.speak("Opening Microsoft Word")
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk')
        return

    elif "excel" in cmd:
        vision.speak("Opening Microsoft Excel")
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk')
        return

    elif "power point" in cmd:
        vision.speak("Opening Microsoft Power Point")
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk')
        return

    elif "calculator" in cmd:
        vision.speak("Opening calculator")
        os.startfile('C:\\Windows\\System32\\calc.exe')
        return

    elif "cmd" in cmd:
        vision.speak("Opening cmd")
        os.startfile('C:\\Windows\\System32\\cmd.exe')
        return

    elif "task manager" in cmd:
        vision.speak("Opening task manager")
        os.startfile('C:\\Windows\\System32\\Taskmgr.exe')
        return

    elif "visual code" in cmd:
        vision.speak("Opening Microsoft Visual Code")
        os.startfile('C:\\Users\\Paras Jetani\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')

    else:
        vision.speak("Application not available")
        return


def close_application(cmd):
    if "word" in cmd:
        vision.speak("Closing Microsoft Word")
        os.system("TASKKILL /F /IM WINWORD.EXE")
        return

    elif "excel" in cmd:
        vision.speak("Closing Microsoft Excel")
        os.system("TASKKILL /F /IM EXCEL.EXE")
        return

    elif "power point" in cmd:
        vision.speak("Closing Microsoft Power Point")
        os.system("TASKKILL /F /IM POWERPNT.EXE")
        return

    elif "calculator" in cmd:
        vision.speak("Closing calculator")
        os.system("TASKKILL /F /IM calculator.exe")
        return

    elif "cmd" in cmd:
        vision.speak("Closing cmd")
        os.system("TASKKILL /F /IM cmd.exe")
        return

    elif "control panel" in cmd:
        vision.speak("Closing control panel")
        os.startfile('C:\\Windows\\System32\\control.exe')
        return

    elif "visual code" in cmd:
        vision.speak("Closing Microsoft Visual Code")
        os.system("TASKKILL /F /IM code.exe")

    else:
        vision.speak("Application not available")
        return
