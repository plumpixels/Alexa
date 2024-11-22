import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import nltk
import os

nltk.download('punkt')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 200)
engine.setProperty('pitch', 1.2)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        query = ""
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        query = ""

    return query




query = listen().lower()

if "joke" in query:
    joke = pyjokes.get_joke()
    speak("Sure, here's a joke for you:")
    speak(joke)

elif "job" in query or "present" in query:
    ppt_path = "D:/amber/Downloads/jobhunt.pptx"
    if os.path.exists(ppt_path):
        speak("Here you go.")
        os.startfile(ppt_path)
        speak("Goodbye, Have a great day ahead !")
    else:
        speak("Sorry, the PowerPoint presentation is not found.")

elif "hello" in query or "hi" in query:
    speak("Hey there ! Anything I can do for you ?")

elif "play" in query:
    song = query.replace("play", "")
    speak("Playing " + song)
    pywhatkit.playonyt(song)

elif "time" in query or "date" in query:
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is " + time)
    date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak("Today's date is " + date)

elif "thanks" in query or "thankyou" in query or "thank you" in query:
    speak("Your welcome. How may I serve you ? ")

elif "goodbye" in query or "good bye" in query:
    speak("Goodbye, Have a great day ahead !")

else:
    tokens = nltk.word_tokenize(query)

    if len(tokens) > 0:

        results = wikipedia.search(query)
        if results:
            speak("Here are the top search results:")
            for i in range(min(2, len(results))):
                speak(results[i])
        else:
            speak("I'm sorry, I couldn't find any information.")

    else:
        speak("Sorry, I didn't get that. Can you please repeat?")
