import random
import pygame
import FctAntoine
from pygame.locals import *

continuer = 1
y = 200
pygame.init()
blanc = (255,255,255)
noir = (0,0,0)
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dino")
carre = pygame.image.load("Test/PetitCarree.png")
yMove = 0

def joueur (carre,x,y) :
    screen.blit(carre,(x,y))


while continuer == 1 :
    for event in pygame.event.get() :
        if event.type == KEYDOWN :
            if event.key == K_SPACE or event.key == K_UP :
                print("Saut")
                yMove = y - 5
            else :
                yMove = y + 5
            if event.key == K_DOWN :
                print("Bas")
            if event.key == K_RETURN :
                continuer = 0
    y += yMove
    pygame.display.update()
    joueur(carre, 200, y)


print ("Fin du Game")
pygame.quit()
quit()