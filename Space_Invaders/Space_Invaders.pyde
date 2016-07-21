paddlex = 400
paddley = 0 
paddlewidth = 80
paddleheight = 25
def setup():
    global paddley,paddlex
    size(800,500)
    paddley = height - 50
    paddlex = width/2 - paddlewidth/2
    
def draw():
    background(0,0,0)
    rect(paddlex,paddley,paddlewidth,paddleheight)
    
def keyPressed():
    
    
    