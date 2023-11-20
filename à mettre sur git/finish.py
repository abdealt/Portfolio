from graphics import *
from pygame import mixer

#variables globales
cases=[[0]*3 for x in range(3)]

def AfficherCrédit():



    fill_screen(noir,f)
    p1=(50,50)
    ecrire("Ce jeu a été créer par:",p1,18,blanc,f)
    p2=(100,100)
    ecrire("ALLAOUAT ABDENOUR",p2,14,blanc,f)
    wait_clic()
    AffichageDebut()


def AffichageDebut():
    mixer.music.load("intro_music.ogg")
    mixer.music.play()

    fill_screen(noir,f)
    p1=(50,50)
    p2=(250,100)
    draw_fill_rectangle(p1,p2,gris,f)
    p1=(70,60)
    ecrire("Commencer à jouer",p1,20,noir,f)
    p3=(50,150)
    p4=(250,200)
    draw_fill_rectangle(p3,p4,gris,f)
    p2=(120,160)
    ecrire("Crédit",p2,20,noir,f)
    p1=(70,230)
    p2=(230,250)
    draw_fill_rectangle(p1,p2,gris,f)
    p2=(125,230)
    ecrire("Quitter",p2,20,noir,f)


def Analyse_clic(p):
    x,y=p
    if 50<=x<=250 and 50<=y<=100:
        return 1

    if 50<=x<=250 and 150<=y<=200:
        return 2

    if 70<=x<=230 and 230<=y<=250:
        pygame.mixer.music.pause()
        return 3
    return 0


def quadrillage():
    pygame.mixer.music.pause()

    mixer.music.load("game_music.ogg")
    mixer.music.play()

    fill_screen(noir,f)
    p1=(100,0)
    p2=(100,300)
    draw_line(p1,p2,blanc,f)

    p1=(200,0)
    p2=(200,300)
    draw_line(p1,p2,blanc,f)

    p1=(0,100)
    p2=(300,100)
    draw_line(p1,p2,blanc,f)

    p1=(0,200)
    p2=(300,200)
    draw_line(p1,p2,blanc,f)


def victoire():
    # test des lignes horizontales pour chacun des joueurs
    for num_joueur in range(1,3):
        for l in range(3):
            if cases[l][0]==num_joueur and cases[l][1]==num_joueur and cases[l][2]==num_joueur:
                return num_joueur
    # test des lignes verticales pour chacun des joueurs
    for num_joueur in range(1,3):
        for c in range(3):
            if cases[0][c]==num_joueur and cases[1][c]==num_joueur and cases[2][c]==num_joueur:
                return num_joueur
    # test des lignes diagonale pour chacun des joueurs
    for num_joueur in range(1,3):
        if cases[0][0]==num_joueur and cases[1][1]==num_joueur and cases[2][2]==num_joueur:
            return num_joueur

    for num_joueur in range(1,3):
        if cases[0][2]==num_joueur and cases[1][1]==num_joueur and cases[2][0]==num_joueur:
            return num_joueur
    return 0


def clic2centre(p):
    x=p[0]//100*100+50
    y=p[1]//100*100+50
    return (x,y)

def centre2pos(centre):
    x,y=centre
    col=x//100
    lig=y//100
    return (lig,col)

def cercle(centre):
    draw_circle(centre,45,rouge,f)

def croix(centre):
    x,y=centre
    p2=(x-45,y-45)
    p3=(x+45,y+45)
    draw_line(p2,p3,bleu,f)
    p2=(x-45,y+45)
    p3=(x+45,y-45)
    draw_line(p2,p3,bleu,f)

#programme principal
f=init_graphics(300,300)
continuer=0
jeu=0
while (continuer!=1):
    AffichageDebut()
    p=wait_clic()
    choix=Analyse_clic(p)
    while (choix==0):
        p=wait_clic()
        choix=Analyse_clic(p)
    if choix==2:
        AfficherCrédit()
    if choix==1:
        jeu=1
    if choix==3:
        continuer=1
    if jeu==1:
        quadrillage()
        coup=0
        while victoire()==0 and coup<9:
            p=wait_clic()
            centre=clic2centre(p)
            l,c=centre2pos(centre)
            while( cases[l][c]!=0):
                p=wait_clic()
                centre=clic2centre(p)
                l,c=centre2pos(centre)

            if coup%2==0:
                cercle(centre)
                cases[l][c]=1
            else:
                croix(centre)
                cases[l][c]=2
            coup=coup+1

        print("Le joueur gagnant est",victoire())


        wait_clic()
        if victoire()==1:
            pygame.mixer.music.pause()

            mixer.music.load("win.ogg")
            mixer.music.play()
            for i in range(301):
                x2=i
                if i<301:
                    y2=i
                else:
                    y2=301
                p1=0,0
                p2=(x2,y2)
                draw_fill_rectangle(p1,p2,rouge,f)
                attendre(2)
            p1=40,150
            ecrire("Bravo Vous Avez Gagné Joueur 1",p1,18,blanc,f)

        if victoire()==2:
            pygame.mixer.music.pause()

            mixer.music.load("win.ogg")
            mixer.music.play()
            for i in range(301):
                x2=i
                if i<301:
                    y2=i
                else:
                    y2=301
                p1=0,0
                p2=(x2,y2)
                draw_fill_rectangle(p1,p2,bleu,f)
                attendre(2)
            p1=40,150
            ecrire("Bravo Vous Avez Gagné Joueur 2",p1,18,blanc,f)


        if victoire()==0:
            pygame.mixer.music.pause()

            mixer.music.load("equal.ogg")
            mixer.music.play()
            for i in range(301):
                x2=i
                if i<301:
                    y2=i
                else:
                    y2=301
                p1=0,0
                p2=(x2,y2)
                draw_fill_rectangle(p1,p2,argent,f)
                attendre(2)
            p1=70,120
            ecrire("C'est Un Match Nul",p1,18,noir,f)
            p1=87,140
            ecrire("Pas De Gagnant",p1,18,noir,f)
            p1=150,160
            ecrire(":(",p1,18,noir,f)
        jeu=0
        cases=[[0]*3 for x in range(3)]
        wait_clic()


pygame.mixer.music.pause()
wait_escape(f)
quit_graphics()
