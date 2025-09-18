import pywhatkit
import wikipedia
import pyjokes

def take_command():

    command = input("You: ").lower()
    if 'alexa' in command:
        command = command.replace('alexa','')
    return command

def run_alexa():
    command = take_command()

    if 'play' in command:
        song = command.replace('play','')
        print('Playing '+ song)
        pywhatkit.playonyt(song)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person,1)
        print(info)
    elif 'joke' in command:
        print(pyjokes.get_joke())
    elif 'shutdown' in command:
        quit()
    else:
        print("I beg your pardon?")

while True:
    print("Hi! I'm Alexa,your Chatbot assistant. Type a command starting with Alexa.")
    run_alexa()
