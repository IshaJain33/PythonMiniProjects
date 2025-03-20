import turtle
import random

screen = turtle.Screen()
screen.title("Turtle Race 🏁")
screen.bgcolor("lightblue")
track = turtle.Turtle()
track.speed(0)
track.penup()
track.goto(-200, 100)
track.pendown()
for i in range(6):
    track.forward(400)
    track.right(90)
    track.forward(50)
    track.right(90)
    track.forward(400)
    track.left(90)
    track.forward(50)
    track.left(90)

track.hideturtle()

# Create turtles
colors = ["red", "blue", "green", "purple", "orange"]
turtles = []

for i in range(5):
    racer = turtle.Turtle()
    racer.color(colors[i])
    racer.shape("turtle")
    racer.penup()
    racer.goto(-200, 75 - (i * 50))
    racer.pendown()
    turtles.append(racer)

# Start race
race_on = True
while race_on:
    for racer in turtles:
        move = random.randint(1, 5)
        racer.forward(move)

        if racer.xcor() >= 200:  # Finish line
            race_on = False
            winner = racer.color()[0]  # Get winner color
            print(f"🏆 The winner is {winner} turtle!")
            break

screen.mainloop()
