import speech_recognition as sr #installed
import webbrowser #inbuilt
import pyttsx3  #installed
import pygame    #installed
import requests #inbuilt
import musicLibrary #user defined
from openai import OpenAI  #installed
import os   #inbuilt
from gtts import gTTS #installed
from pytube import Search #installed

recognizer = sr.Recognizer()
engine=pyttsx3.init()
newsapi = "87751ad413454eeca45be9f3d8fda6a7"

def speak_old(text):      #speak function
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 


def aiProcess(command):
    client = OpenAI(api_key="ijklmnop5678efghijklmnop5678efghijklmnop",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):     # all the diff-diff work commands will be process
    if "google" in c.lower():
        webbrowser.open("https://google.com")
    elif "facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "gmail" in c.lower():
        webbrowser.open("https://gmail.com")
    elif "outlook" in c.lower():
        webbrowser.open("https://outlook.office.com/mail/")
    elif "teams" in c.lower():
        webbrowser.open("https://www.microsoft.com/en-in/microsoft-teams/log-in?msockid=3ec5cf2473ff681d28cfda2e725269c6")

    elif c.lower().startswith("play"):
        song = c.lower().replace("play ", "")
        url = f"https://www.youtube.com/results?search_query={song}"
        webbrowser.open(url)

        
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
        # Parse the JSON response
            data = r.json()
        
        # Extract the articles
            articles = data.get('articles', [])
        
        # Print the headlines
            for article in articles:
                speak(article['title'])
        else:
            speak("Failed to retrieve news")

    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)
    
 
if __name__== "__main__":  #function call will work upon executing this file only
    speak("jarvis is on")
    print("jarvis is on")
    # obtain audio from the microphone
    while True:
        r = sr.Recognizer()
        print("recognizing your input audio you can speak now")
        speak("recognizing your input audio you can speak now")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source: 

                audio = r.listen(source,timeout=2,phrase_time_limit=1)
                word=r.recognize_google(audio)
                 
                
            if "hi" in word.lower() or "hello" in word.lower():
                speak("hello sir how may i help you")

                 #listen for next command
                with sr.Microphone() as source:
                    audio=r.listen(source)
                    print("Jarvis working")
                    speak("I am working on your command")
                    command=r.recognize_google(audio)
                    processCommand(command)
               

        except Exception as e:
            print("Error; {0}".format(e))

            