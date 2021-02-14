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

    # record 10 second to wav file
    talkBot.record(10)

# runs the whole program
main()
