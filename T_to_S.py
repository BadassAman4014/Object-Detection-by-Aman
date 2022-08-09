import pyttsx3
import time
import os
from gtts import gTTS
import threading
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.say("Hi this is working ");
engine.setProperty('voice',voices[0].id)
engine.setProperty('volume',0.9)
engine.runAndWait()
speak=True
item='start'