from random import *
x = 350
y = 350
l = 680
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
    global l
    global m
    global a

    global speed
    background(255)
    
    #switch direction
    if x >= 700:
        xdir = False
        speed = 5
    elif  x <= 0:
        xdir = True
        speed = 5
    if y <= 20:
        ydir = True
        speed = 5
    elif y >= 680:
        ydir = False
        speed = 5
    
        
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
    #bouncing off
 #elif ydir == False:
   #y  = y - speed
    #y += 1
        
    if y == 680:
        if mouseX - 40  < x < mouseX + 100:
            y += 1
    
        '''
    if y == 680 and mouseX < x < mouseX + 100:
        ydir = False
    '''
    rect(mouseX,680,100,-40)
    fill(randrange(255),randrange(255),randrange(255))
    ellipse(x,y,35,45)
    fill(randrange(255),randrange(255),randrange(255))
    
        
    
 
    
    
        
    
    
    
    
    