from random import *
x = 350
y = 350
xdir = False
ydir = True
speed = randint(1,20)
def setup():
    size(700,700)

def draw():
    global xdir
    global ydir
    global x
    global y
    global speed
    background(255)
    
    #switch direction
    if x >= 700:
        xdir = False
        speed = randint(1,20)
    elif  x <= 0:
        xdir = True
        speed = randint(1,20)
    if y <= 25:
        ydir = True
        speed = randint(1,20)
    elif y >= 675:
        ydir = False
        speed = randint(1,20)
    
        
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
    
        

    
   

    ellipse(x,y,35,45)
    fill(randrange(255),randrange(255),randrange(255))
    
    
    
        
    
    
    
    
    