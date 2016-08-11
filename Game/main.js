var BOARD = []; // this keeps track of the whole game
var ROWS, COLS; // number of rows and columns
var SQUARE_SIZE = 30; // size of each square
var FRAME_RATE = 8; // Frame rate (do 8 frames per sec instead of 60)

var UP = 4;
var RIGHT = 1;
var DOWN = 2;
var LEFT = 3;

var PLAYER = []; // list of all the snake bodies
var food; // location of the food in the BOARD list
var EMPTY = 0, SNAKE = 1, FOOD = 2;
var DIR; // Direction the snake is traveling

var GAME_OVER = false;

/*
* This function assigns all the variables and fills
* the board list
*/
function start() {
    COLS = 44;
    ROWS = 21;
    DIR = RIGHT; // the snake starts of going to the right
    GAME_OVER = false;
    PLAYER = [ {x: Math.floor(COLS/2), y: Math.floor(ROWS/2)} ]; // inside the PLAYER list, place an object with x and y coordinate
                // the x and y represents the index of the player's body part in the BOARD list
    BOARD = [];
    // make the BOARD a 2D list
    // and fill it with EMPTY (EMPTY = 0)
    for(var i = 0; i < ROWS; i++){
        var arr = [];
        for(var j = 0; j < COLS; j++){
            arr.push(EMPTY);
        }
        BOARD.push(arr);
    }
    stroke(0, 255, 0);
}

/*
* This function draws all the stuff in the game
* using the BOARD list
*/
function drawBoard() {
    BOARD = [];
    // make everything in the board empty again (set it to 0)
    for(var i = 0; i < ROWS; i++){
        var arr = [];
        for(var j = 0; j < COLS; j++){
            arr.push(EMPTY);
        }
        BOARD.push(arr);
    }

    // if the food exists, then place the food in the BOARD
    // food's x and y is defined in the createFood function
    if(food){
        BOARD[food.y][food.x] = FOOD;
    }

    // loop through all the snake's body parts
    for(var i = 0; i < PLAYER.length; i++){
        // Take the location of each body part
        // then turn that location in the BOARD equal to SNAKE (SNAKE = 1)

        // but only do that if the player is within the boundaries
        if(PLAYER[i].y >=0 && PLAYER[i].y < ROWS && PLAYER[i].x >=0 && PLAYER[i].x < COLS){
            BOARD[PLAYER[i].y][PLAYER[i].x] = SNAKE;
        }
    }

    var a = PLAYER.pop(); // get rid of the last body part (the tail)
    PLAYER.splice(1, 0, a); // put the tail in second position (behind the head)

    // go through all the rows
    for(var y = 0; y < ROWS; y++){
        // go through all of the columns
        for(var x = 0; x < COLS; x++){
            // check what kind of square it is and set the fill color accordingly
            if(BOARD[y][x] == EMPTY){
                fill(255);
            }
            else if(BOARD[y][x] == SNAKE){
                fill(0, 255, 0);
            }
            else if(BOARD[y][x] == FOOD){
                fill(255, 0, 0);
            }
            // finally, draw the rectangle on the screen
            rect(x * SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE);
        }
    }
}

// place a food randomly in the board
function createFood() {
    food = {}; // make food equal to an empty object
    food.x = Math.floor(random(COLS)); // pick random x position and set it to the food's x
    food.y = Math.floor(random(ROWS)); // pick random y position and set it to the food's y

    // if there is a snake where the food is then pick another location for the food
    if(BOARD[food.y][food.x] == SNAKE){
        createFood();
    }
}

function setup() {
    frameRate(FRAME_RATE); // set the frame rate of the game
    start(); // call start before doing anything else since the variables need to be initialized
    createCanvas(COLS * SQUARE_SIZE+1, ROWS * SQUARE_SIZE+1);
    background(119, 120, 120);
    createFood();
}

function draw() {
    drawBoard();
    
    // key input and set player's direction
    if ((key == 'd' || key == 'D' || keyCode == 39) && DIR != LEFT){
        DIR = RIGHT;
    }else if((key == 'a' || key == 'A' || keyCode == 37) && DIR != RIGHT){
        DIR = LEFT;
    }else if((key == 'w' || key == 'W' || keyCode == 38) && DIR != DOWN){
        DIR = UP;
    }else if((key == 's' || key == 'S' || keyCode == 40) && DIR != UP){
        DIR = DOWN;
    }
    // player movement
    if (GAME_OVER == false){ // only move if the game is not over
        if(DIR == RIGHT){
            if(PLAYER.length > 1){ // if the snake has more than a head (at least 2 body parts)
                // take the tail of the snake and make its position equal to where the
                /// head is now
                PLAYER[PLAYER.length-1].y = PLAYER[0].y;
                PLAYER[PLAYER.length-1].x = PLAYER[0].x;
            }
            // then move the head
            PLAYER[0].x++;

            // if the snake went over the boundaries then game is over
            if(PLAYER[0].x > COLS){
                GAME_OVER = true;
            }else{ // otherwise
                // if the player ate a food
                if(BOARD[PLAYER[0].y][PLAYER[0].x] == FOOD){
                    createFood(); // make another food
                    // append another body part to the end of the snake and have its location
                    // equal to the tail's location
                    PLAYER.push( { x: PLAYER[PLAYER.length -1].x, y:PLAYER[PLAYER.length -1].y } );
                }else if(BOARD[PLAYER[0].y][PLAYER[0].x] == SNAKE){ // if the snake hit itself
                    GAME_OVER = true;
                }
            }
        }// repeat this for left, up and down directions
        if(DIR == LEFT){
            if(PLAYER.length > 1){
                PLAYER[PLAYER.length -1].y = PLAYER[0].y;
                PLAYER[PLAYER.length -1].x = PLAYER[0].x;
            }
            PLAYER[0].x --;

            if(PLAYER[0].x < 0){
                GAME_OVER = true;
            }else{
                if(BOARD[PLAYER[0].y][PLAYER[0].x] == FOOD){
                    createFood();
                    PLAYER.push( {x: PLAYER[PLAYER.length -1].x, y:PLAYER[PLAYER.length -1].y} );
                }else if(BOARD[PLAYER[0].y][PLAYER[0].x] == SNAKE){
                    GAME_OVER = true;
                }
            }
        }
        if(DIR == UP){
            if(PLAYER.length > 1){
                PLAYER[PLAYER.length -1].y = PLAYER[0].y;
                PLAYER[PLAYER.length -1].x = PLAYER[0].x;
            }
            PLAYER[0].y --;
            if(PLAYER[0].y < 0){
                GAME_OVER = true;
            }else{
                if(BOARD[PLAYER[0].y][PLAYER[0].x] == FOOD){
                    PLAYER.push( {x: PLAYER[PLAYER.length -1].x, y:PLAYER[PLAYER.length -1].y} );
                    createFood();
                }else if(BOARD[PLAYER[0].y][PLAYER[0].x] == SNAKE){
                    GAME_OVER = true;
                }
            }
        }
        if(DIR == DOWN){
            if(PLAYER.length > 1){
                PLAYER[PLAYER.length -1].y = PLAYER[0].y;
                PLAYER[PLAYER.length -1].x = PLAYER[0].x;
            }
            PLAYER[0].y ++;
            if(PLAYER[0].y >= ROWS){
                GAME_OVER = true;
            }else{
                if(BOARD[PLAYER[0].y][PLAYER[0].x] == FOOD){
                    PLAYER.push( { x: PLAYER[PLAYER.length -1].x, y:PLAYER[PLAYER.length -1].y } );
                    createFood();
                }else if(BOARD[PLAYER[0].y][PLAYER[0].x] == SNAKE){
                    GAME_OVER = true;
                }
            }
        }

        //before drawing the screen, check once again if the player moved out of the
        // boundaries
        if(PLAYER[0].x > COLS){
            GAME_OVER = true;
        }
        if(PLAYER[0].x < 0){
            GAME_OVER = true;
        }
        if(PLAYER[0].y > ROWS){
            GAME_OVER = true;
        }
        if(PLAYER[0].y < 0){
            GAME_OVER = true;
        }
    }else{ // otherwise if the game is over
        if(GAME_OVER){
            // show the "you lost" message 
            fill(0, 157, 255);
            textSize(SQUARE_SIZE * 3);
            var t = "You lost!";
            text(t, width/2 - textWidth(t)/2, height/2);
        }
    }
}