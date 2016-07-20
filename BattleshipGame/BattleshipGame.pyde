from random import *
board = [["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"]]
board[int(randrange(0,5))][int(randrange(5))] = "S" 
def setup():
    size(500,500)
    for i in range(len(board)):
        for j in range(len(board)):
            rect(i*100,j*100,100, 100)

def draw():

 
        
    print(board)
    
    if (mouseButton == LEFT):
        xPos = int(mouseX/100)
        yPos = int(mouseY/100)
        fill(255,0,0)
        rect(xPos*100,yPos*100, 100,100)
            
        print(mouseX)
        print(mouseY)
        
    