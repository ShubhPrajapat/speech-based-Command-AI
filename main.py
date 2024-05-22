import datetime
import pyttsx3
import speech_recognition
import requests
from  bs4 import BeautifulSoup
import os
import pyautogui
import random
import webbrowser 
 
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding....")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"You said:{query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")






if __name__ == "__main__":
    while True:
        query  = takecommand().lower()
        if "wake up" in query:
            from GreetMe import greetme
            greetme()
            
            while True:
                query = takecommand().lower()
                if "go to sleep" in query:
                    speak("ok sir, You can call me anytime")
                    break
                
                elif "hello" in query :
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("as always,good")        
                elif "thank you" in query:
                    speak("You'r welcome,sir")
                elif "tired" in query:
                    speak("playing you favourite songs , enjoy  sir  ")    
                    a= (1,2)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=enb1VYT_-so&list=RDenb1VYT_-so&index=1")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=Nbr_KJT0TIc&list=RDNbr_KJT0TIc&start_radio=1")    
                    
                    
                    
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("vedio paused ,sir")
                elif "play" in query:
                    pyautogui.press("k")    
                    speak("vedio played ,sir")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("vedio muted ,sir")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("turning volume up ,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("turning volume down,sir")
                    volumedown()
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)        
                
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)  
                    
                elif "news" in query:
                    from Newsread import latestnews
                    latestnews()                                                                           
                    
                    
                          
                elif "temperature" in query:
                    search = "temperature in jaipur" 
                    url = (f"https://www.google.com/search?q={search}")
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ ="BNeawe").text  
                    speak(f"current {search} is {temp}")
                elif "weather" in query:
                    search = "temperature in jaipur" 
                    url = (f"https://www.google.com/search?q={search}")
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ ="BNeawe").text    
                    speak(f"current {search} is {temp}")   
                    
                elif "set an alarm" in query:
                    print("input time example:-10 and 10 and 10")
                    speak("set the time")
                    a= input("please tell the time :-")
                    alarm(a)
                    speak("Done,sir")    
                    
                    
                    
                elif "the time" in query: 
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f" sir, {strTime}")  
                elif "turn off" in query:
                    speak("system is shutting down,sir")
                    exit()      
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","") 
                    rememberMessage = query.replace("sai","")
                    speak(f"You told me ,{rememberMessage}")
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember =   open("Remember.txt","r")
                    speak(f"You told me ,{remember.read()}")
                           
                    
                    
                    
                    
                    