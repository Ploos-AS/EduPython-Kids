import random
import turtle

WIDTH = 600
HEIGHT = 400
STEP = 20

score = 0
lives = 3
game_running = True
monster_speed = 6

screen = turtle.Screen()
screen.title("Star Chase")
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("lightblue")

player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()

star = turtle.Turtle()
star.shape("circle")
star.color("gold")
star.penup()

monster = turtle.Turtle()
monster.shape("square")
monster.color("red")
monster.penup()

scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(0, 160)

life_board = turtle.Turtle()
life_board.hideturtle()
life_board.penup()
life_board.goto(-250, 160)

message = turtle.Turtle()
message.hideturtle()
message.penup()


def show_score():
    scoreboard.clear()
    scoreboard.write(f"Score / Poeng: {score}", align="center", font=("Arial", 18, "normal"))


def show_lives():
    life_board.clear()
    life_board.write(f"Lives / Liv: {lives}", font=("Arial", 18, "normal"))


def move_star():
    star.goto(random.randint(-250, 250), random.randint(-150, 150))


def celebrate():
    old_color = star.color()[0]
    star.color("yellow")
    screen.ontimer(lambda: star.color(old_color), 150)


def check_catch():
    global score
    if game_running and player.distance(star) < 25:
        score += 1
        show_score()
        celebrate()
        move_star()


def move_player(dx, dy):
    if not game_running:
        return
    new_x = max(-280, min(280, player.xcor() + dx))
    new_y = max(-180, min(180, player.ycor() + dy))
    player.goto(new_x, new_y)
    check_catch()


def caught():
    global lives
    lives -= 1
    show_lives()
    if lives <= 0:
        game_over()
    else:
        player.goto(0, 0)
        monster.goto(-200, -100)


def move_monster():
    if not game_running:
        return
    monster.setheading(monster.towards(player))
    monster.forward(monster_speed)
    if monster.distance(player) < 25:
        caught()
    screen.ontimer(move_monster, 100)


def game_over():
    global game_running
    game_running = False
    player.hideturtle()
    star.hideturtle()
    monster.hideturtle()
    message.goto(0, 0)
    message.write("GAME OVER", align="center", font=("Arial", 28, "bold"))


screen.listen()
screen.onkey(lambda: move_player(STEP, 0), "Right")
screen.onkey(lambda: move_player(-STEP, 0), "Left")
screen.onkey(lambda: move_player(0, STEP), "Up")
screen.onkey(lambda: move_player(0, -STEP), "Down")

move_star()
monster.goto(-200, -100)
show_score()
show_lives()
move_monster()

turtle.done()
