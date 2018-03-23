import random
import pygame
from pygame.locals import *

continuer = 1

pygame.init()
blanc = (255,255,255)
noir = (0,0,0)
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dino")




while continuer == 1 :
    for event in pygame.event.get() :
        if event.type == KEYDOWN :
            if event.key == K_SPACE or event.type == K_UP :
                print("Saut")
            if event.key == K_RETURN :
                continuer = 0



print ("Fin du Game")
pygame.quit()
quit()