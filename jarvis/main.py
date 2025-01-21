import time
import subprocess
import wolframalpha
import requests
import webbrowser
import wikipedia
import datetime
import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.runAndWait()

# Defining a function for speaking a sentence

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("hello, good morning Mr. Xavier, i wish your day is as pleasant as you are")
        print("hello, good morning Mr. Xavier ")
    elif hour >= 12 and hour <=18:
        speak("hello, Good afternoon Mr. Xavier, Sunny days are always bright")
        print("hello, Good afternoon Mr. Xavier")
    else:
        speak("hello, Good evening Mr. Xavier, its time to rest and go to sleep soon after you are done with me")
        print("hello, Good evening Mr. Xavier")


# Function used to take commands as statements from the voice of a human using laptops in-built Microphone

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("i am listening . . . .")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except:
            speak("pardon me , please say that again")
            return "None"
        return statement


# A Simplified main function
# Add your code blocks here to upgrade this personal assistant. it is 100% modifiable

speak("LOADING YOU PERSONAL AI ASSISTANT JARVIS")
wishMe()



if __name__ == '__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your AI personal assistant JARVIS is shutting down,Good bye')
            print('your AI personal assistant JARVIS is shutting down,Good bye')
            break


        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open for you")
            time.sleep(3)


        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open for you")
            time.sleep(3)


        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://mail.google.com/")
            speak("Google Mail open for you")
            time.sleep(3)

        elif 'chat gpt' in statement:
            webbrowser.open_new_tab("https://chat.openai.com/")
            speak("chat GPT is open for you")
            time.sleep(3)


        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am JARVIS version 1 point O, your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,search wikipedia,predict weather'
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by you")
            print("I was built by you")

        elif "open stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/")
            speak("Here is stackoverflow")
            time.sleep(3)

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India - Happy reading')
            time.sleep(3)

        elif 'bank' in statement:
            bank = webbrowser.open_new_tab("https://www.axisbank.com")
            speak('Here is the details of axis bank')
            time.sleep(3)


        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(3)


        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "love" in statement or "like" in statement:
            speak('You are the person who made me and bring me to this wonderful world, yes i love you too')


        elif "feel" in statement or "feelings" in statement:
            speak('offcourse yes, i want to feel their emotions live & work with humans just to make this world a better place')


        elif "age" in statement or "old" in statement:
            speak('I am still sweet sixteen, and i will be that forever')


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
