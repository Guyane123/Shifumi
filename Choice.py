from Frame import * 
from Shifumi import Shifumi
from random import randint
from Gesture import Gesture, Feuille, Pierre, Ciseau

class Choice():
    def __init__(self, sfm: Shifumi) -> None:
        self._sfm = sfm
        self._choiceTime = 0
        self._isChoice = True
        self._yourChoice = Gesture(-1)
        self._isGeneratedChoice = False
        self._yourChoices = []
        self._myChoices = []
        self._myChoice = Gesture(-1)
    
    def setIsChoice(self, isChoice):
        self._isChoice = isChoice

    def generateChoice(self):
        rdm = randint(0,2)
        self._myChoice = Gesture(rdm)
        print(rdm)
        self._myChoices.append(Gesture(rdm))
        self._isGeneratedChoice = True
        return Gesture(rdm)


    def setYourChoice(self, choice: Gesture):
        self._yourChoice = choice
        self._yourChoices.append(choice)
        self._isChoice = False
        self.generateChoice()
        self._sfm.battle(self._yourChoice, self._myChoice)
        
    def setChoiceTime(self, time):
        self._choiceTime = time
    def getIsChoice(self):
        return self._isChoice
    def getChoices(self):
        return self._yourChoices
    def getYourChoice(self):
        return self._yourChoice
    def getMyChoice(self):
        return self._myChoice
    def getBothChoices(self):
        myChoice = self._myChoice
        yourChoice = self._yourChoice
        return (myChoice, yourChoice)