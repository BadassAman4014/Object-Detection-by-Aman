import cv2
import numpy as np
import random
import pyttsx3
from time import sleep
from threading import *

class detect(Thread):
    def run(self):
        for i in range(5):
            print("detected")
            sleep(1)

class speak(Thread):
    def run(self):
        for i in range(5):
            print("pronounced")
            sleep(1)
t1 = detect()
t2 = speak()

t1.start()
sleep(0.5)
t2.start()

t1.join()
t2.join()