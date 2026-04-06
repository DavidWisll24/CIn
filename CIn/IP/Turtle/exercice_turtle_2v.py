import turtle

turtle.Screen()
t = turtle.Turtle()
t.up()
t.setpos(-600, -350)
t.down()
t.speed(0)
distancia = int(input())
distancia = distancia * 5
x = int(input())
y = int(input())

for i in range(2):
    t.forward(distancia * x)
    t.left(90)
    t.forward(distancia * y)
    t.left(90)

if (x%2 == 1) and x > 1:
    for j in range(x):
        t.forward(distancia)
        t.left(90)
        t.forward(distancia * y)
        t.right(90)
        t.forward(distancia)
        t.right(90)
        t.forward(distancia * y)
        t.left(90)
    t.forward(distancia)

else:
    for j in range(x//2):
        t.forward(distancia)
        t.left(90)
        t.forward(distancia * y)
        t.right(90)
        t.forward(distancia)
        t.right(90)
        t.forward(distancia * y)
        t.left(90)

t.left(90)
if (y%2 == 1) and y > 1:
    for k in range(y//2):
        t.forward(distancia)
        t.left(90)
        t.forward(distancia * x)
        t.right(90)
        t.forward(distancia)
        t.right(90)
        t.forward(distancia * x)
        t.left(90)
    t.forward(distancia)

else:
    for k in range(y//2):
        t.forward(distancia)
        t.left(90)
        t.forward(distancia * x)
        t.right(90)
        t.forward(distancia)
        t.right(90)
        t.forward(distancia * x)
        t.left(90)
        
turtle.done()