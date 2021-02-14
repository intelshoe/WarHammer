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

    # record about 10 seconds and translate to text output
    print(talkBot.record())


# runs the whole program
main()
