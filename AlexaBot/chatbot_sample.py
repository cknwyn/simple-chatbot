import pywhatkit as pwk
import wikipedia as wiki
import pyjokes as pj
import python_weather
import os
import asyncio
import pyttsx3
import requests
from datetime import datetime

# Initialize text-to-speech engine
# engine = pyttsx3.init()


#def speak(text):
#    engine.say(text)
#    engine.runAndWait()


async def get_weather(city) -> None:
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        # Fetch a weather forecast from a city.
        weather = client.get(city)

        # Fetch the temperature for today.
        print(weather.temperature)

        # Fetch weather forecast for upcoming days.
        for daily in weather:
            print(daily)

            # Each daily forecast has their own hourly forecasts.
        for hourly in daily:
            print(f' --> {hourly!r}')


def main():
    try:
        print("Hi! I'm Alexa,your Chatbot assistant. Type a command starting with Alexa.")
        #speak("Welcome to Alexa Chatbot. How can I help you today?")
        user_input = input().lower()

        if not user_input.startswith("alexa"):
            #return speak("Sorry, I couldn't quite catch that.")
            return print("Sorry, I couldn't quite catch that.")

        if "play" in user_input:
            return pwk.playonyt(user_input)

        elif "time" in user_input:
           now = datetime.now()
           time_str = now.strftime("%H:%M:%S")
           print(f"The current time is {time_str}")
           #speak(f"The current time is {time_str}")

        elif "weather" in user_input:
           city = user_input.split("weather in")[-1].strip()
           print(get_weather(city))

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
                return print(wiki.summary(user_input),)

        elif "joke" in user_input:
            joke = pj.get_joke()
            print(joke)
            #speak(joke)

        else:
            #speak("Sorry, I couldn't quite catch that.")
            print("Sorry, I couldn't quite catch that.")

    except Exception as e:
        print(f"Error: {e}")
        #speak("Sorry, I couldn't quite catch that.")


main()
