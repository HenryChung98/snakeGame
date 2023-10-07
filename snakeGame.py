from turtle import Turtle, Screen
import time
import random

done = False
score = 0
speed = 0.05
# screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("Khaki")
screen.title("Snake Game")
screen.tracer(0) # 깜빡이는거 방지


def createSnake(position):
    snake = Turtle()
    snake.shape("square")
    snake.color("orangered")
    snake.up()
    snake.goto(position) # set position
    snakeBody.append(snake)
    

def up():
    if snakeBody[0].heading() != 270:
        snakeBody[0].setheading(90)

def down():
    if snakeBody[0].heading() != 90:
        snakeBody[0].setheading(270)
        
def right():
    if snakeBody[0].heading() != 180:
        snakeBody[0].setheading(0)
        
def left():
    if snakeBody[0].heading() != 0:
        snakeBody[0].setheading(180)


def randPos():
    randX = random.randint(-250, 250)
    randY = random.randint(-250, 250)
    return randX, randY

def scoreUpdate():
    global score
    score += 1
    scorePen.clear()  #이전것 지우고 새로운 값을 다시 보여줘야 됨
    scorePen.write(f"SCORE : {score}", font=("", 15, "bold"))

def gameOver():
        scorePen.goto(0, 0)
        scorePen.write("Game Over", False, "center", ("", 30, "bold"))

# snake
startPos = [(0, 0), (-20, 0), (-40, 0)] 
snakeBody = []


# food
food = Turtle()
food.shape("turtle")
food.color("snow")
food.up()
food.speed(0)
food.goto(randPos())

#score
scorePen = Turtle()
scorePen.ht() #hide turtle
scorePen.up()
scorePen.goto(-270, 250)
scorePen.write(f"SCORE : {score}", font=("", 15, "bold"))
    

    
# keydown event listener
screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(right, "Right")
screen.onkeypress(left, "Left")
    
    
for pos in startPos:
    createSnake(pos)    


while not done:
    screen.update() # screen.tracer와 같이 이용
    
    time.sleep(speed) # 뱀 속도 조절
    if score == 10:
        speed = 0.03
    elif score == 20:
        speed = 0.02
    elif score == 30:
        speed = 0.01
    for i in range(len(snakeBody) -1, 0, -1):
        snakeBody[i].goto(snakeBody[i - 1].pos())
    snakeBody[0].forward(10)
    
    if snakeBody[0].distance(food) < 15: # 둘이 distance가 15px보다 작다면
        food.goto(randPos())
        createSnake(snakeBody[-1].pos())
        scoreUpdate()
        
    if snakeBody[0].xcor() > 280 or snakeBody[0].xcor() < -280 \
       or snakeBody[0].ycor() > 280 or snakeBody[0].ycor() < -280:
        done = True
        gameOver()

                       
    for body in snakeBody[1:]:
        if snakeBody[0].distance(body) < 5:
            done = True
            gameOver() 
                       
        
    
    