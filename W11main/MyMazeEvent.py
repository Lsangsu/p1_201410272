import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.shape("turtle")
wn.bgpic("C:\Users\P400\Desktop\myMaze.gif")
def Keyup():
     t1.fd(50)


def Keydown():
     t1.back(50)


def Keyright():
     t1.right(90)


def Keyleft():
     t1.left(90)


def Mousegoto(x,y):
     t1.setpos(x,y)


def addKeys():
     wn.onkey(Keyup,"Up")
     wn.onkey(Keydown,"Down")
     wn.onkey(Keyright,"Right")
     wn.onkey(Keyleft,"Left")

def addMouse():
     wn.onclick(Mousegoto)

def Mymaze():
	addKeys()
	addMouse()
	wn.listen()
	turtle.mainloop()

Mymaze()
