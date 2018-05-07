def menu():
    boutonJouer = pygame.Rect(100,400,100,20)








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
