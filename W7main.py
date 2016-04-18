import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def drawSquareAtSave(size,pos):
    tracks=list()
    t1.penup()
    t1.setpos(pos,0)
    t1.pendown()
    for i in range(0,4):
        t1.fd(100)
        t1.right(90)
        tracks.append(t1.pos())
    print tracks

def lab7():
    drawSquareAtSave(100,100)

def main():
    lab7()
    

if __name__=="__main__":
	main()
