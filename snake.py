import turtle
import time
import random

#CREATE TITLE AND SCREEN FOR GAME 
delay = 0.1
wn = turtle.Screen()
wn.title("SNAKE")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0) #TURNS OFF SCREEN UPDATES 

#CREATE HEAD FOR SNAKE
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup() #DOESN'T DRAW ANYTHING
head.goto(0,0)
head.direction = "stop"


#BLOCKS FOR THE SNAKE TO EAT 
blocks = turtle.Turtle()
blocks.speed(0)
blocks.shape("square")
blocks.color("green")
blocks.penup() #DOESN'T DRAW ANYTHING
blocks.goto(0,100)

segments = [] #LIST TO ADD TO SNAKE BODY

#WRITE SCORE HEADER 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260) 
pen.write("Score: 0 High Score: 0", align = "center", font = ("Courier", 24, "normal")) #DEFAULT SCORE 

#SCORE KEEPING
score = 0
highscore = 0


#FUNCTIONS FOR MOVING DIRECTIONS 
def move_up():
    if head.direction != "down":
        head.direction = "up"
def move_down():
    if head.direction != "up":
        head.direction = "down"
def move_left():
    if head.direction != "right":
        head.direction = "left"
def move_right():
    if head.direction != "left":
        head.direction = "right"

#FUNCTIONS FOR MOVING SNAKE ON SCREEN
def move():
    if head.direction == "up":
        y = head.ycor() #y coordinate 
        head.sety(y + 20) #moves y coordinate up 20 
    if head.direction == "down":
        y = head.ycor() #y coordinate 
        head.sety(y - 20) #moves y coordinate up 20 
    if head.direction == "left":
        x = head.xcor() #y coordinate 
        head.setx(x - 20) #moves y coordinate up 20 
    if head.direction == "right":
        x = head.xcor() #y coordinate 
        head.setx(x + 20) #moves y coordinate up 20 

        
#KEYBOARD LISTENER 
wn.listen() #WINDOW LISTENING TO KEY PRESSES 
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
#MAIN
while True:
    wn.update() #SCREEN UPDATES EVERYTIME

    #COLLISION CHECKS WITH BORDER 
    if head.xcor() > 290 or head.xcor()<-290 or head.ycor() >290 or head.ycor() <-290: 
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        
        #HIDING SEGMENTS 
        for segments in segments: #GOES THRU LIST OF SEGMENTS ONE AT A TIME 
            segments.goto(1000,1000) #MOVING SEGMENTS TO END OF THE SCREEN 
        #CLEAR SEGMENTS 
        segments = []
    

    #COLLISION CHECKS 
    if head.distance(blocks)<20: #if they collide
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        blocks.goto(x,y)
        
        
        #ADD SEGMENT 
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup() 
        segments.append(new_segment)
        
        #INCREASE SCORE 
        score += 1
        
        if score > highscore:
            highscore = score
        pen.clear()
        pen.write("Score: {} High Score: {}". format(score, highscore), align ="center", font=("Courier",24,"normal"))
        
    #MOVE THE END SEGMENTS FIRST IN REVERSE ORDER
    for i in range(len(segments)-1,0,-1): #COUNTER TO ADD SEGMENTS 
        x = segments[i-1].xcor() #TURTLE HAS X/Y COORDS 
        y = segments[i-1].ycor()
        segments[i].goto(x,y)
        
    #MOVE SNAKE TO START GAME 
    if len(segments) >0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    
    move()

    
      #COLLISION WITH OWN HEAD 
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            
            #RESET SCORE
            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}". format(score, highscore), align ="center", font=("Courier",24,"normal"))
            
    time.sleep(delay)
    
    
wn.mainloop()
