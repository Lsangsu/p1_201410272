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
      
      
def saveTracks():
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    t1.speed(1)
    t1.penup()
    tracks=list()
    t1.goto(-400,300)
    tracks.append(t1.pos())
    t1.pendown()
    t1.pencolor("Red")
    t1.right(90)
    t1.fd(400)
    tracks.append(t1.pos())
    t1.backward(150)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(150)
    tracks.append(t1.pos())
    t1.right(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90)
    t1.right(90)
    t1.right(90)
    t1.fd(200)
    tracks.append(t1.pos())
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(100)
    tracks.append(t1.pos())    
    t1.left(90)
    t1.fd(200)
    tracks.append(t1.pos())
    return tracks
    
    
def replayTracks(Mytracks):
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    t1.speed(1)
    t1.penup()
    t1.goto(-400,300)
    t1.pendown()
    t1.pencolor("Red")
    t1.right(90)
    for i in range(0,len(Mytracks)):
        t1.goto(Mytracks[i])

def lab7():
    drawSquareAtSave(100,(100,100))
    drawSquareAtTrack(50,(-50,-50))
    Mytracks=saveTracks()
    replayTracks(Mytracks)


def main():
    lab7()
    

if __name__=="__main__":
	main()
