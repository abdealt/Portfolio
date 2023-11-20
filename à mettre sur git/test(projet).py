from graphics import *
f=init_graphics(300,300)

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


p1=wait_clic()
x=p1[0]//100*100+50
y=p1[1]//100*100+50
p1=(x,y)
draw_circle(p1,45,rouge,f)
for i in range (4):

    p2=wait_clic()
    x=p2[0]//100*100+50
    y=p2[1]//100*100+50
    p2=(x-45,y-45)
    p3=(x+45,y+45)
    draw_line(p2,p3,bleu,f)
    p2=(x-45,y+45)
    p3=(x+45,y-45)
    draw_line(p2,p3,bleu,f)
    p1=wait_clic()
    x=p1[0]//100*100+50
    y=p1[1]//100*100+50
    p1=(x,y)
    draw_circle(p1,45,rouge,f)


wait_escape(f)
quit_graphics()