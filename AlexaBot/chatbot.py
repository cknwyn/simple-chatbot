import pywhatkit as pwk # general use
import wikipedia as wiki # search wikipedia
import pyjokes as pj # jokes
import pyttsx3 # text to speech use pyttsx3 version 2.91
import requests # make api requests
import os
from dotenv import load_dotenv
from datetime import datetime

# load API key from weatherAPI
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Voice mode
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_weather(city):
    if "today" in city:
        query = "auto:ip" # use ip for location detection
    else:
        query = city

    params = {
        "key": API_KEY,
        "q": query,
        "aqi": "no"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "error" in data:
        return "I could not find the weather for that location."
    
    location = data["location"]["name"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    
    return f"The weather in {location}, {country} is {condition} with {temp_c}°C."
    

def run_alexa(user_input):
    try:
        user_input = user_input.lower()

        if not user_input.startswith("alexa"):
            print("Sorry, I couldn't quite catch that.")
            speak("Sorry, I couldn't quite catch that.")
            return

        if "play" in user_input:
            song = user_input.replace('play','')
            print('Playing '+ song)
            speak('Playing '+ song)
            pwk.playonyt(user_input)

        elif "time" in user_input:
            now = datetime.now()
            time_str = now.strftime("%H:%M:%S")
            print(f"The current time is {time_str}")
            speak(f"The current time is {time_str}")

        elif "weather" in user_input:
            command = user_input.replace("alexa", "").strip()
            city = command.replace("weather", "").strip()
            print(city)
            print(get_weather(city))
            speak(get_weather(city))

        elif any(keyword in user_input for keyword in ["what", "who", "when"]):
            query_location = 0
            match (user_input for keyword in ["what", "who", "when"]):
                case ("who"):
                    query_location = user_input.find("who")
                case ("what"):
                    query_location = user_input.find("what")
                case ("when"):
                    query_location = user_input.find("when")
            check_page = wiki.search(user_input[query_location + 6:])

            print("What are you looking for?")
            for title in check_page:
                print("\t",title)

            user_input = input()
            if user_input in check_page:
                print(wiki.summary(user_input, sentences=5),)
                speak(wiki.summary(user_input, sentences=5),)

        elif "joke" in user_input:
            joke = pj.get_joke()
            print(joke)
            speak(joke)
        
        elif "shutdown" in user_input:
            speak("See you next time!")
            quit()

        else:
            speak("Sorry, I couldn't quite catch that.")
            print("Sorry, I couldn't quite catch that.")

    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I couldn't quite catch that.")

def main():
    speak("Welcome to Alexa Chatbot. How can I help you today?")
    while True:
        user_input = input("Hi! I'm Alexa, your Chatbot assistant. Type a command starting with Alexa.\n")
        run_alexa(user_input)
        
main()