import turtle
import keyboard
# import pyautogui
# ^^^ is for later if needed

running = True # Used to define while loops later
actor = turtle.Turtle() # Defines a turtle
score = 0 # The AI is meant to collect as much of this as possible, sorta like Digital weed.
actor.penup()
actor.speed(100)
# The following code is what the AI supposed to do, such as get score
while running:

    if keyboard.is_pressed("d"):
        actor.setheading(0)
        actor.forward(10)
    if keyboard.is_pressed("a"):
        actor.setheading(180)
        actor.forward(10)
    if keyboard.is_pressed("w"):
        actor.setheading(90)
        actor.forward(10)
    if keyboard.is_pressed("s"):
        actor.setheading(270)
        actor.forward(10)
    if keyboard.is_pressed("u"):
        actor.pendown()
    if keyboard.is_pressed("j"):
        actor.penup()

turtle.mainloop()


