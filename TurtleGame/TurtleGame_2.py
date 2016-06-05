import turtle
import random
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t2.penup()
t2.setpos(-150,-150)
t3=turtle.Turtle()
t3.penup()
t3.setpos(350,-150)
score=50

def turtleLine():
    t2.fd(200)
    t2.left(120)

def StartBox(t3ps):
    if (300<t3ps[0]<400) and (-100<t3ps[1]<0):
        x=random.randint(1,5)
        for i in range(0,x):
            turtleLine()
    else:
        print "Press Black Box!!"
        
def ScoreBox(t2ps):
    if score>150:
        print "Clear!!! Your Score : ", score
            wn.bye()
    elif score<0:
        print "Fail!!"
            wn.bye()
    elif (-150<t2ps[0]<50) and (-50<t2ps[1]<150):
        print "Your Score : ", score+30
            score=score+30
    elif (-250<t2ps[0]<-50) and (-250<t2ps[1]<-50):
        print "Your Score : ", score+10
        score=score+10
    elif (-50<t2ps[0]<150) and (-250<t2ps[1]<-50): 
        print "Your Score : ", score
        
def mousegoto():
    t3.setpos(x,y)
    t3ps=t3.pos()
    StartBox(t3ps)
    t2ps=t2.pos()
    ScoreBox(t2ps)
    
def Game():
    wn.onclick(mousegoto)
    wn.listen()

Game()