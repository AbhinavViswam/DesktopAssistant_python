import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import pyautogui
import time

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold=1.5
        audio=r.listen(source)
        
    try:
        print("Recognising....")
        query=r.recognize_google(audio,language='en-in')
        print("User_said:",query)
    except Exception as e:
        print("Say that again please")
        return "None"
    return query


def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<15:
        speak("good afternoon")

    elif hour>=15 and hour<19:
        speak("good evening")
    else:
        speak("welcome")


def task():
    wishMe()
    speak("We are online and ready")
    while True:
        query=takecommand().lower()

        if "hello" in query or "hai" in query or "hi" in query:
            speak("hello i am your deskstop assistant, hope you are doing well")

        elif "search" in query:
            speak("let me search it in google")
            query=query.replace('search','')
            url="https://google.com/search?q=" + query
            webbrowser.get().open(url)
            speak("Check this please")

        elif "vs" in query or "code" in query:
            path="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(path)
            
        elif 'video of' in query:
            speak("let me search in youtube")
            query=query.replace('video of','')
            url='https://www.youtube.com/results?search_query=' + query
            webbrowser.get().open(url)
            speak("please check this")

        elif 'time' in query:
            t=datetime.datetime.now().strftime("%I:%M:%p")
            speak("Current time is" + t)

        elif 'news' in query:
            speak("let me search")
            url='https://indianexpress.com/'
            webbrowser.get().open(url)
            speak("check this")

        elif 'play song' in query or 'play music' in query:
    
            musicdir='A:\\songs\\'
            songs=os.listdir(musicdir)
            rd=random.choice(songs)
            os.startfile(os.path.join(musicdir,rd))

        
        elif 'mute' in query:
            pyautogui.press("volumemute")

        elif 'unmute' in query:
            pyautogui.press("volumemute")
            speak("Done")

        elif "shutdown the system" in query or 'shutdown system' in query:
            speak("i will shutdown the system for you")
            os.system("shutdown /s /t 5")    
            
        elif "restart the system" in query or 'restart system' in query:
            speak("i will restart the system for you")
            os.system("shutdown /r /t 5")

        elif "open notepad" in query:
            path="C:\\windows\\system32\\notepad.exe"
            speak("opening notepad")
            os.startfile(path)

        elif "sleep" in query or "nap" in query:
            speak("call if you need me")
            break

                
        elif "close notepad" in query:
            speak("closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "screenshot" in query:
            speak("hold the screen, taking screenshot")    
            sshot=pyautogui.screenshot()
            sshot.save("a.jpg")
            time.sleep(1)
            os.startfile("a.jpg")

        elif "kill" in query or "exit" in query:
            speak("ok,hope i worked well")
            speak("see you soon")
            exit()

        elif "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            time.sleep(1)
    
    
task()

if __name__ == "__main__":
    while True:
        permission= takecommand()
        if "wake up" in permission or "makeup" in permission or 'getup' in permission or "get up" in permission:
            task()
