import pywhatkit as pwk
import wikipedia as wiki
import pyjokes as pj

def main():
    #try:
        print("Welcome to Alexa Chatbot")
        user_input = input()
        if not (user_input.capitalize().startswith("Alexa")):
            return print("Sorry, I couldn't quite catch that")
        elif "play" in user_input:
            return pwk.playonyt(user_input, True)
        elif "date" or "time" in user_input:
            # return pwk.info(user_input, 3)
            return
        elif "what" or "who" or "when" in user_input:
            query_location = user_input.find("who")
            print(user_input)
            user_input = user_input[query_location + 1:]
            return print(wiki.summary(user_input, sentences = 5))
        else:
            return
    #except:
        print("Sorry, I couldn't quite catch that")
main()