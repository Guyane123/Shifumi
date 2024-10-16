import Frame, random
from Gesture import *
import pyxel
from Choice import *

class Shifumi():
    def __init__(self):
        self._myScore = 0
        self._yourScore = 0
        self._history = []
    
    def drawScore(self, borderMargin):
        pyxel.text(borderMargin, borderMargin / 2, f'Your score: {self._yourScore}', 7)
        pyxel.text(borderMargin, borderMargin / 2 + 6, f'My score: {self._myScore}', 7)


    def battle(self, yourChoice: Gesture, myChoice: Gesture):


        me = myChoice.getType()
        you = yourChoice.getType()

        self._history.append({myChoice: myChoice, yourChoice: yourChoice})

        if me == 0 and you == 1:
            self._yourScore += 1
        elif me == 1 and you == 0:
            self._myScore += 1
        elif me == 2 and you == 1:
            self._myScore += 1
        elif me == 1 and you == 2:
            self._yourScore += 1
        elif me == 2 and you == 0:
            self._yourScore += 1
        elif me == 0 and you == 2:
            self._myScore += 1

    def getMyScore(self):
        return self._myScore
    def getYourScore(self):
        return self._yourScore



