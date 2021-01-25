import time
import json
from os import system

class betterTuring:

    def __init__(self):
        self.defaultMoves = {'l':-1, 'r':1, '*':0}
        self.rules = None
        self.tape = None
        self.pointerPos = 0
        self.currSign = None
        
