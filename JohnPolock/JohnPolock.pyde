from random import *
def setup():
    size(500,500)
i = 0
def draw():
    rect(mouseX,mouseY,50,70)
    line(mouseX,mouseY,60,100)
    ellipse(randrange(500),randrange(300),randrange(400),randrange(100))
    fill(randrange(255),randrange(255),randrange(255),randrange(255))
    quad(randrange(300),randrange(400),mouseX,mouseY,randrange(100),randrange(500),randrange(400),randrange(500))
    

    
    