import pyttsx3 
import speech_recognition as sr 
import datetime
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# greets the user first
def Greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Sambot. How may I help you?")       

#takes the input from microphone and converts into string
def Listen(): 
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Sorry didn't get you")  
        return "None"
    return query

# performs the said tasks if present in the list
def Instructions():
     while True:
        query = Listen().lower()

        # Logic for executing tasks based on query
        if 'who are you' in query:
            speak("I am Sambot.")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open codechef' in query:
            webbrowser.open("codechef.com")   

        elif 'play music' in query:
            music_dir = 'D:songs\\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'exit' in query:
            speak("Thank you!")
            exit()

#main driver code
if __name__ == "__main__":
    #print("hello")
    #greets the user first
    Greet()
    # to perform the tasks said my user
    Instructions()