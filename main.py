import pyxel
from Gesture import Gesture, Pierre, Feuille, Ciseau
from Frame import *
from Choice import Choice
from Shifumi import Shifumi
import time

SCREEN_WIDTH=128
SCREEN_HEIGHT=128
BORDER_MARGIN = 16
# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Nuit du c0de")
sfm = Shifumi()
c = Choice(sfm)
pyxel.load("my_resource.pyxres")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)


frame_height = SCREEN_HEIGHT / 3 - 16
frame_width = SCREEN_WIDTH / 3 - 16

firstFrame_x = SCREEN_WIDTH / 2 - frame_height / 2
firstFrame_y = SCREEN_WIDTH - frame_width - BORDER_MARGIN

secondFrame_x = SCREEN_WIDTH / 2 - frame_width / 2
secondFrame_y = SCREEN_HEIGHT / 2 - frame_height / 2

thirdFrame_x = 0 + BORDER_MARGIN
thirdFrame_y = SCREEN_HEIGHT / 2 - frame_height / 2


pierre = Frame(firstFrame_y, firstFrame_x, frame_width, frame_height, 1)
feuille = Frame(secondFrame_x, secondFrame_y, frame_width, frame_height, 2)
ciseau = Frame(thirdFrame_x, thirdFrame_y, frame_width, frame_height, 3)

cursor = Frame(pyxel.mouse_x, pyxel.mouse_y, 2,2,7)

frames = [pierre,feuille,ciseau]



#Affiche le curseur
def drawCursor():

    if pierre.colliderect(cursor) or feuille.colliderect(cursor) or ciseau.colliderect(cursor):
        color = 8
        cursor.setColor(color)

    cursor.setX(pyxel.mouse_x)
    cursor.setY(pyxel.mouse_y)

    cursor.draw()


#Affiche les cadres pierre, feuille, ciseau
def drawChoiceFrames():
    for i,el in enumerate(frames):
        el.draw()
        key = ""
        match i:
            case 0:
                key = "P"
            case 1:
                key = "F"
            case 2:
                key = "C"

        pyxel.text(el.getX(),el.getY() + 6 + frame_height, f'Press {key}', 7)


battle_start_frame = None

#Affiche la feunêtre vs
def drawBattleFrames():
    global battle_start_frame

    if battle_start_frame is None:
        battle_start_frame = pyxel.frame_count


    if pyxel.frame_count - battle_start_frame < 60:
        yourChoice = c.getYourChoice()
        myChoice = c.getMyChoice()

        myChoiceFrame = Frame(firstFrame_y, firstFrame_x, frame_width, frame_height, myChoice.getType() + 1)
        yourChoiceFrame = Frame(thirdFrame_x, thirdFrame_y, frame_width, frame_height, yourChoice.getType() + 1)
        pyxel.text(SCREEN_WIDTH / 2 - 4, SCREEN_HEIGHT / 2, "VS", 7)

        myChoiceFrame.draw()
        yourChoiceFrame.draw()
    else:
        c.setIsChoice(True)
        battle_start_frame = None



# Permet de détecter quel geste est utilisé
def handleEvents():
    
    if pyxel.btn(pyxel.KEY_P) or pierre.colliderect(cursor) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        c.setYourChoice(Gesture.Gesture(0))
    if pyxel.btn(pyxel.KEY_F) or feuille.colliderect(cursor) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        c.setYourChoice(Gesture.Gesture(1))
    if pyxel.btn(pyxel.KEY_C) or  ciseau.colliderect(cursor) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        c.setYourChoice(Gesture.Gesture(2))



# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global handleEvents

    # mise à jour de la position du vaisseau
    if c.getIsChoice():
        handleEvents()



# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    
    pyxel.cls(0)

    sfm.drawScore(BORDER_MARGIN)
    

    if c.getIsChoice(): 
        drawChoiceFrames()
    else:
        pyxel.cls(0)
        drawBattleFrames()
    drawCursor()


pyxel.run(update, draw)