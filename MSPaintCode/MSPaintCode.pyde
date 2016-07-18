from random import *
color_choice = 1
def setup():
    size(600,600)
    
def draw():
    global color_choice
    #Red
    fill(255,0,0)
    rect(0,0,75,75)
    #Magenta
    fill(255,0,255)
    rect(75,0,75,75)
    #Blue
    fill(0,0,255)
    rect(150,0,75,75)
    #Cyan
    fill(0,255,255)
    rect(225,0,75,75)
    #Green
    fill(0,255,0)
    rect(300,0,75,75)
    #Yellow
    fill(255,255,0)
    rect(375,0,75,75)
    #Orange
    fill(255,165,0)
    rect(450,0,75,75)

    
    #rainbow
    fill(randrange(255),randrange(255),randrange(255))
    rect(525,0,75,75)
    #---------------------------------------------
    if mouseButton == LEFT:
        #check if the mouseY position is less than 75
        # you are choosing the color
        #mouse X position
        if mouseY < 75:
            if mouseX > 0 and mouseX < 75:
                color_choice = 1
            elif mouseX > 75 and mouseX < 150:
                color_choice = 2
            elif mouseX > 150 and mouseX < 225:
                color_choice = 3
            elif mouseX > 225 and mouseX < 300:
                color_choice = 4
            elif mouseX > 300 and mouseX < 375:
                color_choice = 5
            elif mouseX > 375 and mouseX < 450:
                color_choice = 6
            elif mouseX > 450 and mouseX < 525:
                color_choice = 7
            elif mouseX > 525 and mouseX < 600:
                color_choice = 8
        else:
            if color_choice == 1:
                noStroke()
                fill(255,0,0)
                ellipse(mouseX,mouseY,10,10)
            elif color_choice == 2:
                noStroke()
                fill(255,0,255)
                ellipse(mouseX,mouseY,10,10)
            elif color_choice == 3:
                noStroke()
                fill(0,0,255)
                ellipse(mouseX,mouseY,10,10)
            elif color_choice == 4:
                noStroke()
                fill(0,255,255)
                ellipse(mouseX,mouseY,10,10)
            elif color_choice == 5:
                noStroke()
                fill(0,255,0)
                ellipse(mouseX,mouseY,10,10)
            elif color_choice == 6:
                noStroke()
                fill(255,255,0)
                ellipse(mouseX,mouseY,10,10)
            elif color_choice == 7:
                noStroke()
                fill(255,165,0)
                ellipse(mouseX,mouseY,10,10)
            elif color_choice == 8:
                noStroke()
                fill(randrange(255),randrange(255),randrange(255))
                ellipse(mouseX,mouseY,10,10)
                
            
                
        
        
    
    