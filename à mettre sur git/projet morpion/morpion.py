from graphics import *
f=init_graphics(300,300)

cases=[[0]*3 for x in range(3)]

def quadrillage():
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

def Croix(x1,y1):
    global C1,C2,C3
    Canevas.create_line(x1-45,y1-45,x1+45,y1+45)
    Canevas.create_line(x1+45,y1-45,x1-45,y1+45)
    Verif()
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
def croix():
    if coup%2==0:
        cercle(centre)
        cases[l][c]=1
    else:
        croix(centre)
        cases[l][c]=2
    coup=coup+1

for i in range(300):
    x2=i
    if i<401:
        y2=400
    else:
        y2=400
        p2=(x2,y2)
        draw_fill_rectangle(p1,p2,rouge,f)
        ecrire("Le gagnant est",victoire(1))
print("Le gagnant est",victoire())

p1=(0,0)
for i in range(301):
    x2=i
    if i<401:
        y2=i
    else:
        y2=400
    p2=(x2,y2)
    draw_fill_rectangle(p1,p2,noir,f)
    attendre(2)
p1=90,150
write("le gagnant est",print(victoire),p1,20,blanc,f)

wait_escape(f)
quit_graphics()