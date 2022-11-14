import speech_recognition as speech
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



listener = speech.Recognizer()
engine = pyttsx3.init()


def jarvis_talk(text):
    engine.say(text)
    engine.runAndWait()


# engine.say("Yes sir?")
# engine.say("What can i do for you?")
# engine.runAndWait()

def take_command():
    try:
        with speech.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                # print(command)
    except:
        pass 

    return command


def run_jarvis():
    run_command = take_command()
    if 'play' in run_command:
        song_name = run_command.replace('play', '')
        print("Playing" + song_name)
        jarvis_talk("Playing" + song_name)
        pywhatkit.playonyt(song_name)
    elif 'time' in run_command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print("Current time is " + time)
        jarvis_talk("Current time is " + time)
    elif 'who is' in run_command:
        person = run_command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        jarvis_talk(info)
    elif 'what is' in run_command:
        object = run_command.replace('what is', '')
        info = wikipedia.summary(object, 1)
        print(info)
        jarvis_talk(info)
    elif 'your creator' in run_command:
        print("My creator is Asif")
        jarvis_talk("My creator is Asif")
    elif 'joke' in run_command:
        joke = pyjokes.get_joke()
        print(joke)
        jarvis_talk(joke)
    else:
        print("Please say the command again")
        jarvis_talk("Please say the command again")


while True:
    run_jarvis()