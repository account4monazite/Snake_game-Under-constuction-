import turtle
import time
import random as rd

def gameboy():
    score=0
    high=0

    delay = 0.1

    # Screen setup
    base = turtle.Screen()
    base.title("Snake boiiii")
    base.bgcolor("black")
    base.setup(width=600, height=600)
    base.tracer(0)

    # Snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("red")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"

    # Snake body
    bodyparts = []

    # Food
    nom = turtle.Turtle()
    nom.speed(0)
    nom.shape("circle")
    nom.color("orange")
    nom.penup()
    nom.goto(0, 100)

    # Score

    scoreboard = turtle.Turtle()
    scoreboard.speed(0)

    scoreboard.shape("square")
    scoreboard.color("white")

    scoreboard.penup()
    scoreboard.hideturtle()
    scoreboard.goto(0, 260)
    scoreboard.write(f"Score: {score}  High Score:{high}", align="center", font=("Courier", 24, "normal"))

    # Movement functions
    def goup():
        if head.direction != "down" or head.direction != "right" or head.direction != "left":
            head.direction = "up"

    def godown():
        if head.direction != "up" or head.direction != "right" or head.direction != "left":
            head.direction = "down"

    def goleft():
        if head.direction != "right" or head.direction != "down" or head.direction != "up":
            head.direction = "left"

    def goright():
        if head.direction != "left" or head.direction != "down" or head.direction != "up":
            head.direction = "right"

    def move():
        if head.direction == "up"  :
            y = head.ycor()
            head.sety(y + 20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

    def addbody():
                body = turtle.Turtle()
                body.speed(0)
                body.shape("square")
                body.color("red")
                body.penup()
                bodyparts.append(body)
        

    def transplant():
        for index in range(len(bodyparts)-1, 0, -1):
                x = bodyparts[index-1].xcor()
                y = bodyparts[index-1].ycor()
                bodyparts[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(bodyparts) > 0:
                x = head.xcor()
                y = head.ycor()
                bodyparts[0].goto(x,y)
        

    def update_score():
        scoreboard.clear()
        scoreboard.write(f"Score: {score} High Score: {high}", align="center", font=("Courier", 24, "normal"))

    # Keyboard bindings
    base.listen()
    base.onkeypress(goup, "w")
    base.onkeypress(godown, "s")
    base.onkeypress(goleft, "a")
    base.onkeypress(goright, "d")

    # Main game loop

    while True:
            base.update()
            
            if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                for bawdy in bodyparts:
                    bawdy.goto(1000, 1000)  # Move the body parts off-screen
                bodyparts.clear()
                score = 0
                update_score()

            # Check for collision with food
            if head.distance(nom) < 15:  # Adjusted collision distance
                print("Food eaten! Adding body part...")  # Debugging line
                x = rd.randint(-290, 290)
                y = rd.randint(-290, 290)
                nom.goto(x, y)

                addbody()

                delay -=0.001
                score += 1
                update_score()
                if score>high:
                    high=score

            transplant()

            move()
            # Check for collision with walls
            

            # Check for collision with self
            for bawdy in (bodyparts):
                if bawdy.distance(head) < 20: 
                    print(f"Collision detected with body part ") # Adjusted collision distance
                    
                    print("Game Over!!")
                    time.sleep(1)
                    head.goto(0, 0)
                    head.direction = "stop"
                    for bawdy in bodyparts:
                        bawdy.goto(1000, 1000)  # Move the body parts off-screen
                    bodyparts.clear()
                    score = 0
                    delay=0.1
                    # scoreboard.clear()
                    update_score()
                    

            time.sleep(delay)
    base.mainloop()