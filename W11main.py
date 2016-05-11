import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def Keyup():
	t1.forward(50)
def Keydown():
	t1.back(50)
def Keyright():
	t1.right(90)
def Keyleft():
	t1.left(90)
def End():
	wn.bye()

def mousegoto(x,y):
	t1.setpos(x,y)

def addKeys():
	wn.onkey(Keyup,"Up")
	wn.onkey(Keydown,"Down")
	wn.onkey(Keyright,"Right")
	wn.onkey(Keyleft,"Left")
	wn.onkey(End,"q")

def addMouse():
	wn.onclick(mousegoto)



def lab11():
	addMouse()
	addKeys()
	wn.listen()
	turtle.mainloop()

lab11()