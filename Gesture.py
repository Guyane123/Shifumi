
class Gesture:
    def __init__(self, type: int):
        self._type = type
    
    def typeToText(self):
        match(self._type):
            case -1:
                return "neutral"
            case 0:
                return "pierre"
            case 1:
                return "feuille"
            case 2:
                return "ciseau"
    def getType(self):
        return self._type



Pierre = Gesture(0)
Feuille = Gesture(1)
Ciseau = Gesture(2)
Neutral = Gesture(-1)
