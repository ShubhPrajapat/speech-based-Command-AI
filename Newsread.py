import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def latestnews():
    apidict = {"bussiness" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=51f15d75c3254abf93a35837898fbf70 ",
               "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=51f15d75c3254abf93a35837898fbf70",
               "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=51f15d75c3254abf93a35837898fbf70",
               "sports" : "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=51f15d75c3254abf93a35837898fbf70",
               "technology" : "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=51f15d75c3254abf93a35837898fbf70"}   
    content = None
    url = None
    speak("Which field news do you want to listen ,[bussiness],[entertainment] ,[health],[sports],[technology]")
    field = input("Type news field you want : ")
    for key ,value in apidict.items():
        if key.lower() in field.lower():
            url =  value
            print(url)
            print("url is found")
            break
        else:
            url = True
    if url is True:
        print("url is not found")
    
    news= requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news")
    
    
    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f" for more info visits : {news_url}")
        
        
        a = input("[Press 1 to continue] and [Press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2" :
            break
    
        speak("thats all ")    
                    