def drawSquareAtSave(size,pos):
    import turtle 
    wn = turtle.Screen() 
    t1= turtle.Turtle() 
    tracks=list()
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,4):
        t1.fd(size)
        t1.right(90)
        tracks.append(t1.pos())
    print tracks
    
    
def drawSquareAtTrack(size,pos):
    import turtle 
    wn = turtle.Screen() 
    t1= turtle.Turtle() 
    tracks=list()
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,4):
        t1.fd(size)
        t1.right(90)
        tracks.append(t1.pos())
    t1.home()
    t1.clear()
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,4):
        t1.goto(tracks[i])

def lab7():
    drawSquareAtSave(100,(100,100))
    drawSquareAtTrack(50,(-50,-50))

def main():
    lab7()
    

if __name__=="__main__":
	main()
