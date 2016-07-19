from random import *
x = randint(1,15)
y = randint(1,15)
xdir = True
ydir = True
speed = 5
def setup():
    size(400,400)

def draw():
    global xdir
    global ydir
    global x
    global y
    global speed
    background(255)
    
    #switch direction
    if x >= 375:
        xdir = False
        speed = randint(1,200)
    elif  x <= 25:
        xdir = True
        speed = randint(1,150)
    if y <= 25:
        ydir = True
        speed = randint(1,100)
    elif y >= 375:
        ydir = False
        speed = randint(1,50)
    
        
     #move the ball around   
    if xdir == True:
        x = x + speed
        x -= 1
    elif xdir == False:
        x = x - speed
        x += 1
        #y +- 1
    if ydir == True:
         y = y + speed
         y -= 1
        #x += 1
    elif ydir == False:
        y  = y - speed
        y += 1
    
        
       # x -= 1
    
        

    
   

    rect(x,y,50,50)
    fill(randrange(255),randrange(255),randrange(255))
    
    
    
        
    
    
    
    
    