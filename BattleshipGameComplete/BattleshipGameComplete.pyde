from random import *
board = [["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"]]
board[int(randrange(0,5))][int(randrange(5))] = "S"

lives = 10 
def setup():
    size(500,500)
    for i in range(len(board)):
        for j in range(len(board)):
            rect(i*100,j*100,100, 100)

def draw():
    global lives
    if lives == 0:
        textSize(50)
        text("You lost",100,100)
def mousePressed():
    global board
    global lives
    if (mouseButton == LEFT):
        xPos = int(mouseX/100)
        yPos = int(mouseY/100)
        if board[xPos][yPos] == "S":
            # this will run if the user finds the ship
            fill(255,0,0)
            rect(xPos*100,yPos*100, 100,100)        
            textSize(30)
            text("You win", 200, 400)
            
        else:
        #this will happen if the player does not find the ship
            print("you missed")
            xPos = int(mouseX/100)
            yPos = int(mouseY/100)
            fill(0,255,0)
            rect(xPos*100,yPos*100,100,100)
            lives = lives - 1
        
            
    print(mouseX)
    print(mouseY)