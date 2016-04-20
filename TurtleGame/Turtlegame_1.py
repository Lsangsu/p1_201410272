import turtle
import random
wn=turtle.Screen()
wn.bgpic("upup.gif")
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t1.shape("turtle")
t1.pencolor("red")
t1.left(135)
t1.speed(1)
t2.shape("turtle")
t2.pencolor("blue")
t2.left(135)
t2.speed(1)
t3.pencolor("green")
redwin=0
bluewin=0
tracks=tuple
tracks=((200,-340),(160,-300),(120,-260),(80,-220),(40,-180),(0,-140),(-40,-100),(-80,-60),(-120,-20),(-160,20))
SRP=['scissors','rock','paper']
t1.setpos(tracks[0])
t2.setpos(tracks[0])

def box(size,pos):
     t3.penup()
     t3.setpos(pos)
     t3.pendown()
     t3.fd(size)
     t3.right(90)
     t3.fd(size)
     t3.right(90)
     t3.fd(size)
     t3.right(90)
     t3.fd(size)
     t3.right(90)

def drawStarAt(size,pos):
     t3.penup()
     t3.setpos(pos)
     t3.pendown()
     t3.right(144)
     t3.fd(size)
     t3.right(144)
     t3.fd(size)
     t3.right(144)
     t3.fd(size)
     t3.right(144)
     t3.fd(size)
     t3.right(144)
     t3.fd(size)
        
box(100,(-250,300))
print "Let's play up stairs game~"
ask=raw_input ("press Enter to start")
print " "

for i in range(0,3):               
    t1.setpos(tracks[0])
    t2.setpos(tracks[0])
    t1.clear()
    t2.clear()
    sum1=0
    sum2=0
    x=0
    y=0
    
    for i in range(0,100):
        red=random.choice(SRP)
        blue=random.choice(SRP)
        if sum1==9 or sum2==9:
            if sum1==9:
                t1.goto(-200,270)
            else:
                t2.goto(-200,270)
            break
        elif red==blue:
            sum1=sum1+0
            sum2=sum2+0
        elif red == 'scissors':
            if blue == 'rock':
                t2.goto(tracks[y+1])
                y=y+1
                sum2=sum2+1
            else:
                t1.goto(tracks[x+1])
                x=x+1
                sum1=sum1+1
        elif red == 'rock':
            if blue == 'paper':
                t2.goto(tracks[y+1])
                y=y+1
                sum2=sum2+1
            else:
                t1.goto(tracks[x+1])
                x=x+1
                sum1=sum1+1
        elif red == 'paper':
            if blue == 'rock':
                t1.goto(tracks[x+1])
                x=x+1
                sum1=sum1+1
            else:
                t2.goto(tracks[y+1])
                y=y+1
                sum2=sum2+1       
    if (-250,300)<t1.pos() and t1.pos()<(-150,200):
        print"Red Turtle got 1 point"
        redwin=redwin+1
    elif (-250,300)<t2.pos() and t2.pos()<(-150,200):
        print"Blue Turtle got 1 point"
        bluewin=bluewin+1
        
t1.setpos(-100,0)
t2.setpos(100,0)
t1.clear()
t2.clear()
t3.clear()

print" "        
print "Red Turtle point : ", redwin
print "Blue turtle point : ",bluewin 
if redwin>bluewin:
    print "Red Turtle is Winner"
    drawStarAt(100,(-50,15))
else:
    print "blue Turtle is Winner"
    drawStarAt(100,(150,15))