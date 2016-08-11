var x = 350;
var y = 350;
var xdir = false;
var ydir = true;
var speed = Math.floor((Math.random() * 20) + 1);
function setup(){
	createCanvas(700,700);
}

function draw(){
	background(255,0,0);
	if (x >= 700){
		xdir = false;
	} else if(x <= 0){
		xdir = true;
	}
	if ( y >= 20){
		ydir = true;
	} else if( y >= 60){
		ydir = false;
	}
	//move the ball around
	if (xdir == true){
		x = x + speed;
		x -= 1;
	} else if (xdir == false){
		x = x - speed;
		x += 1
	} if( ydir == true){
		y = y + speed;
		y -= 1;
	} else if(ydir == false){
		y = y - speed;
		y += 1;
	}
	//bouncing off
	if(y == 680){
		while(mouseX - 100 < x < mouseX + 100){
			ydir == false;
		}
		} else{
		(ydir == true)
	}

	if(ydir == false){
		y = y - speed;
		y -= 1;
	}
	if(y == 680){
		if(mouseX -= 40 < x < mouseX + 100){
			y += 1;
		}
	}
	if(y == 680 && mouseX < x < mouseX + 100){
		xdir == false;
	}

	rect(mouseX, 600, 100,20);
	color(random(0,255),random(0,255),random(0,255));
	ellipse(x,y,35,45);
	color(random(0,255),random(0,255),random(0,255));

}