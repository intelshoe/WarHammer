#!/usr/bin/env python3

'''
WarHammer - a modern phreaker's war dialing sword.

Status: under construction.
'''

import speech_recognition as sr

# obtain audio from the microphone
# requires PyAudio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# write audio to a WAV file
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())