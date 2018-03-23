import pygame
from pygame import *

pygame.init()
mixer.init()

blanc = (255,255,255)
noir = (0,0,0)
size = width, height = 800, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dino")

bg = pygame.image.load('bapt/bg.jpg')
bg1 = pygame.image.load('bapt/menu.jpg')

font = pygame.font.Font('bapt/BradBunR.ttf',160)
font1 = pygame.font.Font('bapt/BradBunR.ttf',50)
font2 = pygame.font.Font('bapt/BradBunR.ttf',20)

def jouer():
    verge



def commandes():
    phallus


def classement():
    bite



def info():
        screen.blit(bg,[0,0])
        Gt = font.render("Dino",1,blanc)
        Pt = font1.render("Cliquez pour continuer",1,blanc)
        screen.blit(Gt,(250,200))
        screen.blit(Pt,(200,500))

def menu():
    screen.blit(bg1,[0,0])
    Gt1 = font.render("Menu",1,blanc)
    Pt1 = font1.render("Jouer",1,blanc)
    Pt2 = font1.render("Commandes",1,blanc)
    Pt3 = font1.render("Classement",1,blanc)
    Pt4 = font2.render("Cree par Baptiste Camoes, Arthur Dubuet, Antoine Desfaits",1,blanc)
    screen.blit(Pt4,(360,550))
    screen.blit(Pt3,(100,500))
    screen.blit(Pt2,(100,450))
    screen.blit(Pt1,(100,400))
    screen.blit(Gt1,(30,0))



etat = 'info'

continuer = 1

while continuer:

    if etat == 'info':
        info()
    if etat == 'menu':
        menu()


    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

        if event.type == MOUSEBUTTONDOWN:
            if event.button ==1:
                etat = 'menu'


pygame.quit()
quit()