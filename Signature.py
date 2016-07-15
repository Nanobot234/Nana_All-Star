from Myro import *
init("sim")
penUp()
forward(1,5)
penDown()
def triangle():
    i = 0
    while i < 3:
        turnBy(120,"deg")
        forward(1,2)
        i = i + 1
triangle()
turnBy(90,"deg")
def square():
    i = 0
    while i < 4:
        forward(1,2)
        turnBy(90,"deg")
        i = i + 1
square()
turnBy(90,"deg")
forward(1,3)
turnBy(60, "deg")

motors(0,1,25)
def shape():
    i = 0
    while i < 3:
        forward(1,3)
        turnBy(120,"deg")
        i = i + 1
shape()