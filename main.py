#!/usr/bin/env python3

'''
This section records audio

Needs work:
break parts into class
'''
import speech_recognition as sr
import time
from os import path

def speachToTxt():
    # obtain audio from the microphone
    # requires PyAudio (only supports python 3.6)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    time.sleep(10)

    #  making a change to show you
    #making a change!!!

    # write audio to a WAV file
    with open("microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())

    # begin code to transcribe audio to text
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "microphone-results.wav")

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("I think I heard: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return

def main():
    speachToTxt()

main()
