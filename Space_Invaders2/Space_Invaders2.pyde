paddlex = 400
paddley = 0 
paddlewidth = 80
paddleheight = 8
paddlespeed = 10
bulletx = 0
bullety = 0
bulletspeed = 15
bulletsize = 10
playershooting = False
def setup():
    global paddley,paddlex
    size(800,500)
    paddley = height - 30
    paddlex = width/2 - paddlewidth/2
    noStroke()
def draw():
    global paddlex,paddley,playershooting,bulletx,bullety,bulletsize
    background(0,0,0)
    triangle(paddlex,paddley,paddlex + paddlewidth/2,paddley-10,paddlex + paddlewidth,paddley)
    rect(paddlex,paddley,paddlewidth,paddleheight)
    if playershooting == True:
        fill(0,255,255)
        ellipse(bulletx,bullety,bulletsize,bulletsize)
        
def keyPressed():
    #see if player pressed left or right an move the ship
    global paddlex,paddlespeed,paddlewidth,paddley,playershooting,bulletx,bullety
    if keyCode == 39:
        paddlex += paddlespeed
    elif keyCode == 37:
        paddlex -= paddlespeed
    print(keyCode)
    
    if paddlex <= 0:
        paddlex = 0
    elif paddlex + paddlewidth > width:
        paddlex =  width - paddlewidth
      #pressing space   
    if keyCode == 32:
        playershooting = True
        bulletx = paddlex
        bulletx = paddley
        print(playershooting)
    
        
    
    
    #right = 39,left = 37
    
    
    