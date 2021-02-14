'''
Main interface to features.

Talk.record(secondsToRecord)

Talk.type(secondsToRecord | recording)

Talk.play(soundToPlay)

'''
import speech_recognition as sr
import time
from os import path

class Talk():
    def __init__(self):
        seconds = 0

    def __str__():
        return "Talk Options"

    # saves audio to wav file
    def record(self, seconds):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        time.sleep(seconds)
        # write audio to a WAV file
        with open("microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())
