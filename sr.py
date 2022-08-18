import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('volume',0.9)
r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            if (format(text)=="hello"):        
                engine.say("Hello Master");
                engine.runAndWait()
            elif(format(text)=="quit"):
                engine.say("See You sir");
                break
            else:
                engine.say(format(text));
                engine.runAndWait()
        except:
            print("Sorry could not recognize what you said")