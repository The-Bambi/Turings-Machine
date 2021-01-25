import time
import json
from termcolor import colored
from os import system

class turing:
    def __init__(self, inp = None, rules = None):
        self.tape = list(inp)
        self.pointerPos = 0
        self.defaultMoves = {'l':-1, 'r':1, '*':0}
        self.instr = rules
        self.sign = None
        self.state = '0'

    def step(self):

        if self.state == "halt":
            return 'halt'

        p = self.pointerPos
        if self.pointerPos < 0:
            self.pointerPos = 0
            p = 0
            self.tape = [' '] + self.tape
        elif p > len(self.tape) - 1:
            self.tape += [' ']

        self.sign = self.tape[p]
        
        if '*' in self.instr[self.state].keys():
            instruction = self.instr[self.state]['*']
        else:
            try:
                instruction = self.instr[self.state][self.sign]
            except KeyError:
                 raise Exception('no instruction {} for sign {}'.format(self.state, self.sign))
        if instruction['newSign'] != '*':
            self.tape[p] = instruction['newSign']
        else:
            pass

        self.state = instruction['newState']
        self.pointerPos += self.defaultMoves[instruction['move']]
        return instruction

    def show(self):
        tapestr = ' '.join(self.tape)
        pointstr = ' ' * (self.pointerPos * 2) + '^'
        print(tapestr + '\n' + pointstr)
        self.printRules()
        print('state: '+self.state)

    def stepByStep(self, step = 0.2):
        system('clear')
        self.show()
        time.sleep(step)
        instr = self.step()
        while instr != 'halt':
            instr = self.step()
            system('clear')
            self.show()
            print("current rule: {} {} {} {} {}".format(self.state, self.sign, instr['newSign'], instr['move'], instr['newState']))
            time.sleep(step)
        return

    def printRules(self):
        for state in self.instr:
            for symbol in self.instr[state]:
                rule = self.instr[state][symbol]
                print("{} {} {} {} {}".format(state, symbol, rule['newSign'], rule['move'], rule['newState']))

    def loadInstr(self, path):
        with open(path, 'r') as file:
            self.instr = json.load(file)
            file.close()
