
import speech_recognition as sr

r = sr.Recognizer() 
while True:
    with sr.Microphone() as source:
        print('Hola, soy tu asistente por voz: ')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="es-ES")
            print('Has dicho: {}'.format(text))
            print(text)
        except:
            print('No te he entendido')