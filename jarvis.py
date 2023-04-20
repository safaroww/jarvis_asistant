# import speech_recognition as speech
# import pyttsx3
# import pywhatkit
# import datetime
# import wikipedia
# import pyjokes



# listener = speech.Recognizer()
# engine = pyttsx3.init()


# def jarvis_talk(text):
#     engine.say(text)
#     engine.runAndWait()


# # engine.say("Yes sir?")
# # engine.say("What can i do for you?")
# # engine.runAndWait()

# def take_command():
#     try:
#         with speech.Microphone() as source:
#             print("Listening...")
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             if 'jarvis' in command:
#                 command = command.replace('jarvis', '')
#                 # print(command)
#     except:
#         pass 

#     return command


# def run_jarvis():
#     run_command = take_command()
#     if 'play' in run_command:
#         song_name = run_command.replace('play', '')
#         print("Playing" + song_name)
#         jarvis_talk("Playing" + song_name)
#         pywhatkit.playonyt(song_name)
#     if 'hello' in run_command:
#         print("Hello")
#         jarvis_talk("Hello")
#     elif 'time' in run_command:
#         time = datetime.datetime.now().strftime('%I:%M %p')
#         print("Current time is " + time)
#         jarvis_talk("Current time is " + time)
#     elif 'who is' in run_command:
#         person = run_command.replace('who is', '')
#         info = wikipedia.summary(person, 1)
#         print(info)
#         jarvis_talk(info)
#     elif 'what is' in run_command:
#         object = run_command.replace('what is', '')
#         info = wikipedia.summary(object, 1)
#         print(info)
#         jarvis_talk(info)
#     elif 'your creator' in run_command:
#         print("My creator is Asif")
#         jarvis_talk("My creator is Asif")
#     elif 'joke' in run_command:
#         joke = pyjokes.get_joke()
#         print(joke)
#         jarvis_talk(joke)
#     else:
#         print("Please say the command again")
#         jarvis_talk("Please say the command again")


# while True:
#     run_jarvis()


# /////////////////////////////////////////


import speech_recognition as speech
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

class Jarvis:
    def __init__(self):
        self.listener = speech.Recognizer()
        self.engine = pyttsx3.init()
        
    def jarvis_talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def take_command(self):
        try:
            with speech.Microphone() as source:
                print("Listening...")
                voice = self.listener.listen(source)
                command = self.listener.recognize_google(voice)
                command = command.lower()
                if 'jarvis' in command:
                    command = command.replace('jarvis', '')
        except:
            command = None

        return command


    def run_jarvis(self):
        while True:
            run_command = self.take_command()
            if 'play' in run_command:
                song_name = run_command.replace('play', '')
                print("Playing" + song_name)
                self.jarvis_talk("Playing" + song_name)
                pywhatkit.playonyt(song_name)
            elif 'hello' in run_command:
                print("Hello")
                self.jarvis_talk("Hello")
            elif 'time' in run_command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print("Current time is " + time)
                self.jarvis_talk("Current time is " + time)
            elif 'who is' in run_command:
                person = run_command.replace('who is', '')
                try:
                    info = wikipedia.summary(person, 1)
                    print(info)
                    self.jarvis_talk(info)
                except wikipedia.exceptions.PageError:
                    print(f"Sorry, I couldn't find any information on {person}.")
                    self.jarvis_talk(f"Sorry, I couldn't find any information on {person}.")
            elif 'what is' in run_command:
                object = run_command.replace('what is', '')
                try:
                    info = wikipedia.summary(object, 1)
                    print(info)
                    self.jarvis_talk(info)
                except wikipedia.exceptions.PageError:
                    print(f"Sorry, I couldn't find any information on {object}.")
                    self.jarvis_talk(f"Sorry, I couldn't find any information on {object}.")
            elif 'your creator' in run_command:
                print("My creator is Asif")
                self.jarvis_talk("My creator is Asif")
            elif 'joke' in run_command:
                joke = pyjokes.get_joke()
                print(joke)
                self.jarvis_talk(joke)
            elif 'shut up' in run_command or 'stop' in run_command:
                self.jarvis_talk("Goodbye!")
                return
            else:
                print("Please say the command again")
                self.jarvis_talk("Please say the command again")

if __name__ == '__main__':
    jarvis = Jarvis()
    jarvis.run_jarvis()
