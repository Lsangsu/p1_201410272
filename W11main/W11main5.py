import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t1.shape("turtle")
line=[(50,99),(150,101)]
xy=(0,0)
def OnLine():
    t2.penup()
    t2.goto(50,99)
    t2.pendown()
    t2.forward(100)
    t2.left(90)
    t2.forward(2)
    t2.left(90)
    t2.forward(100)
    t2.left(90)
    t2.forward(2)

OnLine()

def isinRectangle(xy,line):
    xs=line[0][0]
    xe=line[1][0]
    ys=line[0][1]
    ye=line[1][1]
    if xs<=xy[0]<=xe and ys<=xy[1]<=ye:
        t1.pencolor("red")
        print "true"
    else:
        t1.pencolor("black")
        print "false"

def Keyup():
    t1.fd(5)
    pt=t1.pos()
    isinRectangle(pt,line)

def Keydown():
    t1.back(5)
    pt=t1.pos()
    isinRectangle(pt,line)
    
def Keyright():
     t1.right(90)

def Keyleft():
     t1.left(90)

def Mousegoto(x,y):
    t1.setpos(x,y)
    pt=t1.pos()
    isinRectangle(pt,line)

def addKeys():
     wn.onkey(Keyup,"Up")
     wn.onkey(Keydown,"Down")
     wn.onkey(Keyright,"Right")
     wn.onkey(Keyleft,"Left")
    
def addMouse():
     wn.onclick(Mousegoto)

def W11main5():
     wn.listen()
     addKeys()
     addMouse()
     turtle.mainloop()

W11main5()