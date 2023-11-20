import pygame
from pygame.locals import *
pygame.init()
from math import *
from random import *

#Variable globale d'affichage automatique
AFFICHE_AUTO=True

def affiche_auto_off():
    global AFFICHE_AUTO
    AFFICHE_AUTO=False

def affiche_auto_on():
    global AFFICHE_AUTO
    AFFICHE_AUTO=True

def affiche_all():
    pygame.display.flip()

def wait_clic():
    ev=pygame.event.wait()
    while(ev.type!=MOUSEBUTTONDOWN):
        ev=pygame.event.wait()
    return ev.pos

def wait_escape(fenetre):
    continuer=True
    while (continuer):
             attendre(200)
             p1=(10,10)
             ecrire("Appuyer sur echap pour terminer",p1,14,gris,fenetre)
             for evt in pygame.event.get():
                 if evt.type == pygame.locals.QUIT:
                     continuer = False
                 elif evt.type == pygame.locals.KEYDOWN and evt.key == K_ESCAPE:
                     continuer = False
             continue
    return

def fill_screen(couleur,fenetre):
    largeur=fenetre.get_width()
    hauteur=fenetre.get_height()
    p1=(0,0)
    p2=(largeur,hauteur)
    draw_fill_rectangle(p1,p2,couleur,fenetre)

def draw_pixel(point,couleur,fenetre):
    fenetre.set_at(point,couleur)
    if AFFICHE_AUTO:
        pygame.display.flip()

def draw_ellipse(point1,point2,couleur,fenetre):
    x1=min(point1[0],point2[0])
    y1=min(point1[1],point2[1])
    x2=max(point1[0],point2[0])
    y2=max(point1[1],point2[1])
    rect=((x1,y1),(x2-x1,y2-y1))
    pygame.draw.ellipse(fenetre, couleur, rect, 1)

def draw_fill_ellipse(point1,point2,couleur,fenetre):
    x1=min(point1[0],point2[0])
    y1=min(point1[1],point2[1])
    x2=max(point1[0],point2[0])
    y2=max(point1[1],point2[1])
    rect=((x1,y1),(x2-x1,y2-y1))
    pygame.draw.ellipse(fenetre, couleur, rect, 0)

def draw_rectangle(point1,point2,couleur,fenetre):
    x1=min(point1[0],point2[0])
    y1=min(point1[1],point2[1])
    x2=max(point1[0],point2[0])
    y2=max(point1[1],point2[1])
    r=((x1,y1),(x2-x1,y2-y1))
    pygame.draw.rect(fenetre,couleur,r,1)
    if AFFICHE_AUTO:
        pygame.display.flip()

def draw_fill_rectangle(point1,point2,couleur,fenetre):
    x1=min(point1[0],point2[0])
    y1=min(point1[1],point2[1])
    x2=max(point1[0],point2[0])
    y2=max(point1[1],point2[1])
    r=((x1,y1),(x2-x1,y2-y1))
    pygame.draw.rect(fenetre,couleur,r,0)
    if AFFICHE_AUTO:
        pygame.display.flip()

def draw_fill_circle(centre,rayon,couleur,fenetre):
    pygame.draw.circle(fenetre,couleur,centre,rayon,0)
    if AFFICHE_AUTO:
        pygame.display.flip()

def draw_circle(centre,rayon,couleur,fenetre):
    pygame.draw.circle(fenetre,couleur,centre,rayon,1)
    if AFFICHE_AUTO==True:
        pygame.display.flip()

def draw_line(point1,point2,couleur,fenetre):
    pygame.draw.line(fenetre,couleur,point1,point2)
    if AFFICHE_AUTO:
        pygame.display.flip()

def init_graphics(largeur,hauteur):
    if largeur>1024:
        largeur=800
    if hauteur>720:
        hauteur=600
    fenetre=pygame.display.set_mode((largeur,hauteur))
    return fenetre

def attendre(millisecondes):
    pygame.time.wait(millisecondes)

def ecrire(texte,point,taille,couleur,fenetre):
    font=pygame.font.SysFont('arial', taille)
    text = font.render(texte,0,couleur)
    fenetre.blit(text, point)
    pygame.display.flip()

def ecrire_nombre(nombre,point,taille,couleur,fenetre):
    ecrire(str(nombre),point,taille,couleur,fenetre)

def quit_graphics():
    pygame.display.quit()

def distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

#Pour un nombre aleatoire entre 0 et 1 taper random()

# Retourne un entier aleatoire n tel que min <= n <= max
def alea_int(min,max):
    return randint(min,max)

#variables couleur 18 principales
vert=(0,255,0)
rouge=(255,0,0)
bleu=(0,0,255)
cyan=(0,255,255)
blanc=(255,255,255)
jaune=(255,255,0)
orange=(255,165,0)
noir=(0,0,0)
argent=(192,192,192)
bleumarine=(0,0,128)
citronvert=(0,255,0)
magenta=(255,0,255)
gris=(128,128,128)
marron=(128,0,0)
sarcelle=(0,128,128)
vertclair=(0,128,0)
vertolive =(128,128,0)
violet=(128,0,128)

# 140 couleurs en anglais
aliceblue=(240,248,255)
antiquewhite=(250,235,215)
aqua=(0,255,255)
aquamarine=(127,255,212)
azure=(240,255,255)
beige=(245,245,220)
bisque=(255,228,196)
black=(0,0,0)
blanchedalmond=(255,235,205)
blue=(0,0,255)
blueviolet=(138,43,226)
brown=(165,42,42)
burlywood=(222,184,135)
cadetblue=(95,158,160)
chartreuse=(127,255,0)
chocolate=(210,105,30)
coral=(255,127,80)
cornflowerblue=(100,149,237)
cornsilk=(255,248,220)
crimson=(220,20,60)
darkblue=(0,0,139)
darkcyan=(0,139,139)
darkgoldenrod=(184,134,11)
darkgray=(169,169,169)
#define darkgreen            0x006400
#define darkkhaki            0xBDB76B
#define darkmagenta          0x8B008B
#define darkolivegreen       0x556B2F
#define darkorange           0xFF8C00
#define darkorchid           0x9932CC
#define darkred              0x8B0000
#define darksalmon           0xE9967A
#define darkseagreen         0x8FBC8F
#define darkslateblue        0x483D8B
#define darkslategray        0x2F4F4F
#define darkturquoise        0x00CED1
#define darkviolet           0x9400D3
#define deeppink             0xFF1493
#define deepskyblue          0x00BFFF
#define dimgray              0x696969
#define dodgerblue           0x1E90FF
#define firebrick            0xB22222
#define floralwhite          0xFFFAF0
#define forestgreen          0x228B22
#define fuchsia              0xFF00FF
#define gainsboro            0xDCDCDC
#define ghostwhite           0xF8F8FF
#define gold                 0xFFD700
#define goldenrod            0xDAA520
#define gray                 0x808080
#define green                0x008000
#define greenyellow          0xADFF2F
#define honeydew             0xF0FFF0
#define hotpink              0xFF69B4
#define indianred            0xCD5C5C
#define indigo               0x4B0082
#define ivory                0xFFFFF0
#define khaki                0xF0E68C
#define lavender             0xE6E6FA
#define lavenderblush        0xFFF0F5
#define lawngreen            0x7CFC00
#define lemonchiffon         0xFFFACD
#define lightblue            0xADD8E6
#define lightcoral           0xF08080
#define lightcyan            0xE0FFFF
#define lightgoldenrodyellow 0xFAFAD2
#define lightgreen           0x90EE90
#define lightgrey            0xD3D3D3
#define lightpink            0xFFB6C1
#define lightsalmon          0xFFA07A
#define lightseagreen        0x20B2AA
#define lightskyblue         0x87CEFA
#define lightslategray       0x778899
#define lightsteelblue       0xB0C4DE
#define lightyellow          0xFFFFE0
#define lime                 0x00FF00
#define limegreen            0x32CD32
#define linen                0xFAF0E6
#define magenta              0xFF00FF
#define maroon               0x800000
#define mediumaquamarine     0x66CDAA
#define mediumblue           0x0000CD
#define mediumorchid         0xBA55D3
#define mediumpurple         0x9370DB
#define mediumseagreen       0x3CB371
#define mediumslateblue      0x7B68EE
#define mediumspringgreen    0x00FA9A
#define mediumturquoise      0x48D1CC
#define mediumvioletred      0xC71585
#define midnightblue         0x191970
#define mintcream            0xF5FFFA
#define mistyrose            0xFFE4E1
#define moccasin             0xFFE4B5
#define navajowhite          0xFFDEAD
#define navy                 0x000080
#define oldlace              0xFDF5E6
#define olive                0x808000
#define olivedrab            0x6B8E23
#define orange               0xFFA500
#define orangered            0xFF4500
#define orchid               0xDA70D6
#define palegoldenrod        0xEEE8AA
#define palegreen            0x98FB98
#define paleturquoise        0xAFEEEE
#define palevioletred        0xDB7093
#define papayawhip           0xFFEFD5
#define peachpuff            0xFFDAB9
#define peru                 0xCD853F
#define pink                 0xFFC0CB
#define plum                 0xDDA0DD
#define powderblue           0xB0E0E6
#define purple               0x800080
#define red                  0xFF0000
#define rosybrown            0xBC8F8F
#define royalblue            0x4169E1
#define saddlebrown          0x8B4513
#define salmon               0xFA8072
#define sandybrown           0xF4A460
#define seagreen             0x2E8B57
#define seashell             0xFFF5EE
#define sienna               0xA0522D
#define silver               0xC0C0C0
#define skyblue              0x87CEEB
#define slateblue            0x6A5ACD
#define slategray            0x708090
#define snow                 0xFFFAFA
#define springgreen          0x00FF7F
#define steelblue            0x4682B4
#define tan                  0xD2B48C
#define teal                 0x008080
#define thistle              0xD8BFD8
#define tomato               0xFF6347
#define turquoise            0x40E0D0
#define violetlight          0xEE82EE
#define wheat                0xF5DEB3
#define white                0xFFFFFF
#define whitesmoke           0xF5F5F5
#define yellow               0xFFFF00
#define yellowgreen          0x9ACD32
