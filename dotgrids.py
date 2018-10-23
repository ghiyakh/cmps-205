#7. dot grids

import turtle
turtle.speed(100)

import sys
n=int(sys.argv[1])
length=int(sys.argv[2])

def dot_grid(n, length): 
#n: num of rows and col // length of the side of the grid
    empty_grid(n, length)
    draw_circles(n, length)

def draw_circles(n, length):
    l = length/n
    turtle.shape("circle")
    for i in range(n):
        for j in range(n):
            turtle.up()
            turtle.setposition(l*(0.5+i), l*(0.5+j))
            turtle.down()
            if (i+j)%2==0:
                turtle.color("black")
            else:
                turtle.color("red")
            turtle.stamp()

def empty_grid(n, length):
    l = length/n
    for i in range(n):
        turtle.up()
        turtle.setposition(0, i*l)
        turtle.down()
        for j in range(n):
            unit_square(l)

def unit_square(l): 
#l: length of side of each unit ( l=lenght/n )
    for i in range(4):
        turtle.forward(l)
        turtle.left(90)
    turtle.forward(l)




import random
colors = ["red","yellow","blue","green","black"]

def cdot_grid(n, length, colors):
    empty_grid(n, length)
    draw_colored_circles(n, length, colors)
    x = random.choice(colors)
    turtle.color(x)

def draw_colored_circles(n, length, colors):
    l = length/n
    turtle.shape("circle")
    for i in range(n):
        for j in range(n):
            turtle.up()
            turtle.setposition(l*(0.5+i), l*(0.5+j))
            turtle.down()
            turtle.color(random.choice(colors))
            turtle.stamp()



dot_grid(n, length)

cdot_grid(n, length, colors)

turtle.done()