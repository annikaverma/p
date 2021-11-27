from tkinter import *
import speech recognition as sr
import pytttsx3
from datetime import datetime


root = Tk()
root.geometry("500x500")

text_to_speech=pyttsx3.init()

def speak(audio):
    speak("How can i help you?")
    speech_recognisor= sr.Recognizer()
    with sr.Microphone() as source:
        audio= speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data= speech_recognisor.recognize_google(audio,language='en-in')
        except sr.UnknownValueError:
            print("Please repeat i did not get that")
            speak("Please repeat i did not get that")

    respond(voice_data)

def respond(voice_data):
    voice_dta = voice_data.lower()
    print(voice_data)
    if "name" in voive_data:
        speak("My name ia Jarvis")
        print('My name ia Jarvis')

    if "time" in voice_data:
        speak("Current Time is")
        now = datetime.now.strftime(%H.%M.%S")
        speak(current_time)
        print(current_time)

r_audio()

root.mainloop()
