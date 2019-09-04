import turtle
bob=turtle
bob.color("black")
bob.speed(20)
def square():
    for i in range(4):
        bob.forward(100)
        bob.right(90)

square()

for i in range(30):
    square()
    bob.right(5)

bob.color("red")
for i in range(30):
    square()
    bob.right(5)

bob.exitonclick()