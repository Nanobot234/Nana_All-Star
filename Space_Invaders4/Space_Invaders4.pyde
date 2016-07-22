paddleX = 400 #Where the x position is
paddleY = 0 #The y position of where the paddle starts, the beginning left corner
paddleWidth = 80 #How long paddle is
paddleHeight = 8 #
paddleSpeed = 10

playerShooting = False
bulletX = 0
bulletY = 0
bulletSpeed = 20
bulletSize = 10
enemies = []
enemyX = 100
enemyY = 50
enemyDistance = 10
enemySize = 50
enemySpeed = 3
SpeedX = 1
hits = 0
lost = False
# 1: square
#2 :triangle

def setup():
    global paddleY, paddleX, paddleWidth,enemies
    size(800, 500)
    noStroke()
    paddleY = height - 30
    paddleX = (width / 2) - (paddleWidth / 2)
    #put enemies in 2d list
    enemies.append([1] * 10)
    enemies.append([1] * 10)
    enemies.append([0] * 2 + [1] * 6 + [0] * 2)
#def findLastLivingEnemy():
  # global enemies
   # last = -1
    #for i in range(len(enemies), -1, -1):
        
    
def draw():
    global paddleX, paddleY, paddleWidth, paddleHeight, bulletX, bulletY, bulletSpeed, bulletSize, playerShooting,enemies
    global enemyX,enemyY,enemyDistance,enemySize,enemySpeed,SpeedX,hits,lost
    #making the shapes
    background(0, 0, 0)
    rect(paddleX, paddleY, paddleWidth, paddleHeight)
    triangle(paddleX, paddleY, paddleX + paddleWidth/2, paddleY - 10, paddleX+paddleWidth, paddleY)
  
  
    for y in range(len(enemies)):
        for x in range(len(enemies[y])):
            if enemies [y][x] == 1:
                fill(255,0,0)
                rect((x*enemySize+enemyX) + (x * enemyDistance), (y*enemySize+enemyY) + (y* enemyDistance),enemySize,enemySize)
                
    enemyX += SpeedX
    
    x = (len(enemies[0]))
    
    if (x*enemySize+enemyX) + (x * enemyDistance) >= width:
        if SpeedX > 2:
            SpeedX *= -1.01
        else:
            SpeedX *= -1
            enemyY += enemyDistance
    elif enemyX <= 0:
        SpeedX *= -2
        enemyY += enemyDistance
    
    
    #for 
    
            
    if playerShooting == True:
        fill(0, 255, 255)
        ellipse(bulletX, bulletY, bulletSize, bulletSize)
        bulletY -= bulletSpeed
        if bulletY <= 0:
            playerShooting = False
        for y in range(len(enemies)):
            for x in range(len(enemies[y])):
                if(enemies[y][x] == 1):
                    distance = dist(bulletX,bulletY, (x*enemySize + enemyX) + (x*enemyDistance) + (enemySize/2),(y*enemySize + enemyY) + (y*enemyDistance) + (enemySize/2))
                    if distance < enemySize/2:
                        enemies[y][x] = 0
                        playerShooting = False
                        hits = hits + 1
                        break
                        
                        
    fill(255, 255, 255)
    
    if hits == 26:
        textSize(50)
        fill(210,160,40)
        text("You Win",200,200)
    l = len(enemies)
    if hits == 15:
        bulletSize = bulletSize + 0.5
        bulletSpeed = bulletSpeed + 1
   
    if (l*enemySize+enemyY) + (y*enemyDistance) >= paddleY:
        lost = True
        
    if lost == True:
        textSize(30)
        fill(240,220,0)
        text("You were defeated by aliens",width/2 -150,height/2)
        playerShooting = False
    

#If keypressed happens
def keyPressed():
    # see if the player pressed left or right arrow key and then move the ship to the right or left
    # right = 39, left = 37
    global paddleX, paddleY, paddleSpeed, paddleWidth, bulletX, bulletY, playerShooting
    if keyCode == 39:
        paddleX += paddleSpeed
    elif keyCode == 37:
        paddleX -= paddleSpeed
        
    # if the player is pressing space, then shoot
    if keyCode == 32:
        if playerShooting == False:
            playerShooting = True
            bulletX = paddleX + paddleWidth/2
            bulletY = paddleY  - 10
            
        
        
    # check if the paddle is going off the screen
    # if yes, then put the paddle in the screen
    if paddleX <= 0:
        paddleX = 0
    elif paddleX + paddleWidth >= width:
        paddleX = width - paddleWidth
    
    
    