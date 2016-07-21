from random import *
import time
board = [["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"]]
board[int(randrange(0,8))][int(randrange(5))] = "S"
board[int(randrange(0,8))][int(randrange(5))] = "S"

lives = 1
hits = 0
def setup():
    size(800,500)

def draw():
    global lives
    global board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if  board[i][j] == 1:
                fill(0,255,0)
                rect(i*100,j*100,100, 100)
            elif board[i][j] == 2:
                fill(255,255,0)
                ellipse(i*100 + 50,j*100 + 50,100,100)
            else:
                fill(255,255,255)
                rect(i*100,j*100,100, 100)
    textSize(20)
    fill(0,0,0)
    text("Lives remaining:" + str(lives),300,50)
    if lives <= 0:
        textSize(50)
        text("You lost",100,100)
    if hits == 2:
        textSize(30)
        text("You win",100,100)        
def mousePressed():
    global board
    global lives
    global hits
    if lives > 0 and hits < 2:
        if (mouseButton == LEFT):
            xPos = int(mouseX/100)
            yPos = int(mouseY/100)
            if board[xPos][yPos] == "S":
                # this will run if the user finds the ship
                board[xPos][yPos] = 2
                fill(255,0,0)
                rect(xPos*100,yPos*100, 100,100)        
                hits = hits + 1
            else:
            #this will happen if the player does not find the ship
                print("you missed")
                xPos = int(mouseX/100)
                yPos = int(mouseY/100)
                board[xPos][yPos] = 1
                fill(0,255,0)
                rect(xPos*100,yPos*100,100,100)
                lives = lives - 1
                
            
            
        
            
    print(mouseX)
    print(mouseY)