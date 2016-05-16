import turtle
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t1.shape("turtle")
coord=[(100,100),(200,200)]
curpos=(0,0)
def rectangle(size):
    t2.penup()
    t2.goto(100,100)
    t2.pendown()
    t2.forward(100)
    t2.left(90)
    t2.forward(100)
    t2.left(90)
    t2.forward(100)
    t2.left(90)
    t2.forward(100)

rectangle(100)

def isinRectangle(curpos,coord):
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    if xs<=curpos[0]<=xe and ys<=curpos[1]<=ye:
        t1.pencolor("red")
	print "true"
    else:
        t1.pencolor("black")
	print "false"

def Keyup():
    t1.fd(50)
    pt=t1.pos()
    isinRectangle(pt,coord)

def Keydown():
    t1.back(50)
    pt=t1.pos()
    isinRectangle(pt,coord)
    
def Keyright():
     t1.right(90)

def Keyleft():
     t1.left(90)

def Mousegoto(x,y):
    t1.setpos(x,y)
    pt=t1.pos()
    isinRectangle(pt,coord)

def addKeys():
     wn.onkey(Keyup,"Up")
     wn.onkey(Keydown,"Down")
     wn.onkey(Keyright,"Right")
     wn.onkey(Keyleft,"Left")
    
def addMouse():
     wn.onclick(Mousegoto)

def W11main4():
     wn.listen()
     addKeys()
     addMouse()
     turtle.mainloop()

W11main4()
