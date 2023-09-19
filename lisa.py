import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('What can I do for you?')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'lisa' in command:
                command = command.replace('lisa', '')
                print(command)
                
    except:
        pass
    return command


def run_lisa():
    command = take_command()
    print(command)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('It is ' + time)
        print('It is ' + time)
        
    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'what' in command:
        thing = command.replace('what', '')
        info = wikipedia.summary(thing,1)
        print(info)
        talk(info)
    elif 'where' in command:
        place = command.replace('where' , '')
        info = wikipedia.summary(place,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
        print('I am in a relationship with wifi')
    elif 'how are you' in command:
        talk('I am fine! How are you?')
        print('I am fine! How are you?')
    elif 'introduce yourself' in command:
        talk('I am lisa, a simple virtual assistand!')
        print('I am lisa, a simple virtual assistand!')
    else:
        talk('Please try again:')
        print('Please try again:')


run_lisa()
