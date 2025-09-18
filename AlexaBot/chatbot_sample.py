import pywhatkit as pwk
import wikipedia
import wikipedia as wiki
import pyjokes as pj
import pyttsx3
import requests
from datetime import datetime

# Initialize text-to-speech engine
# engine = pyttsx3.init()


#def speak(text):
#    engine.say(text)
#    engine.runAndWait()


#def get_weather(city):
#   api_key = "YOUR_API_KEY"
#   url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
#   response = requests.get(url)
#   data = response.json()
#   if data["cod"] == "404":
#       speak("City not found.")
#       return "City not found."
#   else:
#       main_data = data["main"]
#       temperature = main_data["temp"] - 273.15  # Convert from Kelvin to Celsius
#       speak(f"The temperature in {city} is {temperature:.2f}°C")
#       return f"The temperature in {city} is {temperature:.2f}°C" '''


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

        elif any(keyword in user_input for keyword in ["what", "who", "when"]):
            query_location = 0
            match (user_input for keyword in ["what", "who", "when"]):
                case ("who"):
                    query_location = user_input.find("who")
                case ("what"):
                    query_location = user_input.find("what")
                case ("when"):
                    query_location = user_input.find("when")
            check_page = wikipedia.search(user_input[query_location + 6:])

            #summary = wiki.summary(user_input[query_location + 7:], sentences=5, auto_suggest=False)
            print("What are you looking for?")
            for title in check_page:
                print("\t",title)

            user_input = input()
            if user_input in check_page:
                return print(wiki.summary(user_input),)

        #elif "weather" in user_input:
        #   city = user_input.split("weather in")[-1].strip()
        #   print(get_weather(city))

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
