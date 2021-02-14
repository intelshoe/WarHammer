#!/usr/bin/env python3
'''
Main app entry point.

'''
import speech_recognition as sr
import time
from os import path
from talk import Talk

def main():
    # start the talking feature
    talkBot = Talk()

    # records for 5 seconds, saves to wav file and returns the text
    print(talkBot.record(5, "testing"))


# runs the whole program
main()
