from datetime import datetime
from operator import truediv
import webbrowser
import pyttsx3 as p
import speech_recognition as sr
import pandas as pd
import os

time = datetime.now().strftime("%H:%M")
eng = p.init('sapi5')
voice = eng.getProperty('voices')
eng.setProperty('voice', voice[0].id)

data = pd.read_csv("C:\\Users\\DELL\\Desktop\\myWorkSpace\\virbroo\\command.csv",index_col="command")
df = pd.DataFrame(data)
commands = df.to_dict()

def hello():
    time = datetime.now().strftime("%H")
    day = datetime.now().strftime("%A")
    speak("Hii sir")
    d=''
    time = int(time)
    if time < 12 and time >= 0:
        speak("good morning")
        d='morning'
    elif time >= 12 and time < 17:
        speak("good afternoon")
        d='afternoon'
    else:
        speak("good evening")
        d='noon'
    speak("its "+day+" "+d+" "+str(24-time)+" O clock")


def speak(audio):
    print("speaking'.......")
    print(audio)
    eng.say(audio)
    eng.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
      
        print("listening....")
        audio = r.listen(source, phrase_time_limit=5)
        print("recognizing.....")
        query = r.recognize_google(audio, language="en-in")
        query = query.lower()
        return query


def tellTime(time):
    print(time)
    speak(time)

def todo():
    data = pd.read_csv("C:\\Users\\DELL\\Desktop\\myWorkSpace\\virbroo\\todo.csv",index_col="time")
    df = pd.DataFrame(data) 
    t = datetime.now().strftime("%H")
    speak(df.loc[int(t)]["activity"])


if __name__=="__main__":
    hello()
    while True:
        try:    
            query = take_command()
            print(query)
            if 'youtube' in query:
                print(query)
                speak("opening youtube")
                webbrowser.open("youtube.com")
            # elif 'google' or "connect me to internet" in query:
            #     print(query)
            #     speak("opening google")
            #     webbrowser.open("google.com")
            elif 'time' in query:
                tellTime(time)
            elif "activity" in query:
                todo()
            elif "tic tak toe" in query:
                speak("enjoy playinng the game")
            elif "exit" in query:
                speak("turning off")
                speak("tata")
                break

            else:
                flag=0
                for i in commands["do"]:
                    if i in query:
                        
                        flag=1
                        break
                if flag == 1:
                    com = commands["do"][i]
                    print(i)
                    if "open" in i:
                        speak("opening")
                        os.system(com)
                    else:
                        speak(com)
                else:
                    speak("sorry")
                    speak("command not found")
                   
        except:
            speak("sorry unable to recognize")
            speak("say again")