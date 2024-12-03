import webbrowser
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
            
            # para abrir amazon si dices amazon
            if 'Amazon' in text:
                webbrowser.open('https://www.amazon.com')
            elif "cállate" in text.lower():
                print("Cerrando programa")
                break
            if 'libros' in text:
                webbrowser.open('https://www.fnac.es')
            elif 'cállate' in text:
                print("Cerrando programa")
                break
        except:
            print('No te he entendido')