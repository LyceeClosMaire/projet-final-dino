import pygame
from pygame import *

pygame.init()
mixer.init()

blanc = (255,255,255)
noir = (0,0,0)
size = width, height = 800,600
etat='info'

xa = 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dino")

bg = pygame.image.load('bapt/bg.jpg')
bg1 = pygame.image.load('bapt/menu.jpg')
bgf = pygame.image.load('bapt/defiler2.png')


font = pygame.font.Font('bapt/BradBunR.ttf',160)
font1 = pygame.font.Font('bapt/BradBunR.ttf',50)
font2 = pygame.font.Font('bapt/BradBunR.ttf',20)

def jouer():
    screen.blit(bgf,(xa,0))



def commandes():
    screen.blit(bg,[0,0])
    Pt5 = font1.render("tu as juste à sauter avec espace connard",1,blanc)
    screen.blit(Pt5,(0,300))


def classement():
    screen.blit(bg,[0,0])



def info():
    global etat
    screen.blit(bg,[0,0])
    Gt = font.render("Dino",1,blanc)
    Pt = font1.render("Cliquez pour continuer",1,blanc)
    screen.blit(Gt,(250,200))
    screen.blit(Pt,(200,500))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button ==1:
                etat='menu'


def menu():
    global etat
    screen.blit(bg1,[0,0])
    boutonJouer = pygame.Rect(100,400,100,100)
    Pt1 = font1.render("Jouer",1,blanc)
    screen.blit(Pt1,(100,400))
    boutonCommandes = pygame.Rect(100,450,100,100)
    Pt2 = font1.render("Commandes",1,blanc)
    screen.blit(Pt2,(100,450))
    boutonClassement = pygame.Rect(100,500,100,100)
    Pt3 = font1.render("Classement",1,blanc)
    screen.blit(Pt3,(100,500))



    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button ==1:
                mousepos=pygame.mouse.get_pos()
                if boutonJouer.collidepoint(mousepos):
                    etat = 'jouer'
                if boutonCommandes.collidepoint(mousepos):
                    etat = 'commandes'
                if boutonClassement.collidepoint(mousepos):
                    etat = 'classement'

    Gt1 = font.render("Menu",1,blanc)
    screen.blit(Gt1,(30,0))
    Pt4 = font2.render("Cree par Baptiste Camoes, Arthur Dubuet, Antoine Desfaits",1,blanc)
    screen.blit(Pt4,(360,550))

continuer = 1

while continuer:
        if xa == -12000:
            xa = 0
        else:
            xa -= 1
        if etat == 'commandes' and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            etat = 'menu'

        if etat == 'info':
              info()
        elif etat == 'menu':
              menu()
        elif etat == 'jouer':
                jouer()
        elif etat == 'commandes':
            commandes()
        elif etat == 'classement':
            classement()

        pygame.display.flip()
        pygame.display.update()

        for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    continuer=0


pygame.quit()
quit()