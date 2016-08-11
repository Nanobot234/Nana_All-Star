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
        speed = 5
    elif  x <= 0:
        xdir = True
        speed = 5
    if y >= 20:
        ydir = True
        speed = 5
    elif y >= 60:
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
    elif ydir == False:
        y = y - speed
        y += 1
        
    '''
    elif ydir == False and mouseX - 100 < x < mouseX + 100:
            y = y - speed
            y += 1 
    '''
    #bouncing off
    
    if y == 680:
        while mouseX - 100 < x < mouseX + 100:
            ydir == False
        else:
            ydir == True
            
        if ydir == False:
            y  = y - speed
            y -= 1 
    
        
        
    if y == 680:
        if mouseX - 40  < x < mouseX + 100:
            y += 1
    
    
    if y == 680 and mouseX < x < mouseX + 100:
        ydir = False
    
    rect(mouseX ,680 ,100,-20)
    fill(randrange(255),randrange(255),randrange(255))
    ellipse(x,y,35,45)
    fill(randrange(255),randrange(255),randrange(255))
    
        
    
 
    
    
        
    
    
    
    
    