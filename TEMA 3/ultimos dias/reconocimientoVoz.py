
import webbrowser
import speech_recognition as sr
from gtts import gTTS
import pyttsx3

r = sr.Recognizer() 
while True:
    with sr.Microphone() as source:
        print('Hola, soy tu asistente por voz: ')
        audio = r.listen(source)
 
        try:
            text = r.recognize_google(audio, language="es-ES")
            print('Has dicho: {}'.format(text))
            print(text)
            if "Amazon" in text:
                webbrowser.open('http://amazon.es')
            if "noticias" in text:
                webbrowser.open('http://elmundo.es')
            if "qué tal" in text:
                engine = pyttsx3.init()
                engine.say("Bien y tú?")
                engine.runAndWait()
                print("Bien y tu?")
        except:
            print('No te he entendido')