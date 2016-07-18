x = 0
y = 0
xdir = True
ydir = True
def setup():
    size(400,400)

def draw():
    global x
    global y
    global xdir
    global ydir
    if x == 255:
        xdir = False
    elif x == 0:
        xdir = True  
    if xdir == False:
        y += 1
    elif xdir == True:
        x += 1
    

    rect(x,y,50,50)