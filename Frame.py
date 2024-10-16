import pyxel, Gesture
class Frame:
    def __init__(self, x: int, y: int, w: int ,h: int, bgColor: int):
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._bgColor = bgColor

    def draw(self):
        pyxel.rect(self._x, self._y, self._w, self._h, self._bgColor)
        

    def colliderect(self, secondEl: 'Frame') -> bool:

        if (self._x < secondEl.getX() + secondEl.getW() and
            self._x + self._w > secondEl.getX() and
            self._y < secondEl.getY() + secondEl.getH() and
            self._y + self._h > secondEl.getY()):
            return True
        return False
    
    def setX(self, x):
        self._x = x
    def setY(self, y):
        self._y = y
    def setW(self, w):
        self._w = w
    def setH(self, h):
        self._w = h
    def setColor(self, color: int):
        self._bgColor = color

    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getW(self):
        return self._w
    def getH(self):
        return self._h
    
