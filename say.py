"""
from sayings  import hello
import sys

if len(sys.argv) == 2:
    #cowsay.cow("hello, " +sys.argv[1])
    #cowsay.trex("hello" +sys.argv[1])
    hello(sys.argv[1])

## But its executing the whole program and main gets called

# so we used __name__ = "__main__"

"""

import cowsay
import pyttsx3

engine = pyttsx3.init()

this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()

