var snake = [0];
var x = 0;
var y = 0;
var xSpeed = 25;
var ySpeed = 25;
var rectRandX = Math.floor((Math.random() * 775) + 1);
var rectRandY = Math.floor((Math.random() * 475) + 1); 
var snake_count = 0;
var totalBlack = 0;
var blue = Math.floor((Math.random() * 255) + 1);
var red = Math.floor((Math.random() * 255) + 1);
var green = Math.floor((Math.random() * 255) + 1);
//Makes food
function makeRect(){
	fill(1, 0, 0);
	rect(rectRandX,rectRandY,25,25);
}
//Checks the pixel value o
function checkColor(pixels,value){
 	var count_value = 0;
 	for(var l=0;l<=pixels.length;l++){
 		if(pixels[l]==value) 
 			count_value+=1;
 	}
 return count_value;

}


function setup(){
	createCanvas(800,500);
	makeRect();
	loadPixels();	//smakeRect();
	totalBlack = checkColor(pixels, 1);
	//alert(totalBlack);
}

function draw(){
	background(0,255,0);
	makeRect();
	//for(i in range(len(board[i])));
	//drawing box	
	fill(1,0,0);
	rect(rectRandX,rectRandY,25,25);

	//drawing the growing snake
	 
		
	
	
	if(snake[0] == 0){
		fill(255,0,0);
		rect(x,y,25,25);
		//fill(1,0,0);
		//rect(rectRandX,rectRandY,25,25);
	}

	/*
	if(snake[1] == 1){ 
		//alert("Your right");
		fill(0, 0, 255);
		rect(x - 25 ,y,25,25); 
	}
*/
	if (keyCode =="39" && x < 775){
		x += xSpeed;
	}
	//if(keyCode == 65 && x < width){
	if(keyCode == "37" && x > 0) {
		x -= xSpeed;
	}
	
	//if(keyCode == 83 && y > height){
	if(keyCode == "38" && y >= 0) {
		y -= ySpeed;
	}
	
	//if(keyCode == 87 && y < height){
	if(keyCode == "40" && y < 475) {
		y += ySpeed;

	}
	loadPixels();
	if(checkColor(pixels, 1) < totalBlack){
		/*	appen
		for(var i=0; i<=snake.length; i++){
		if(snake[i]==snake_count){
			fill(255,0,0);
			rect(x - i*25,y,25,25);
		}
		
		
	}
	*/
		//adding to tail of snake
		//append(snake,snake_count);

		append(snake,snake_count);
		

		rectRandX = Math.floor((Math.random() * 775) + 1);
		rectRandY = Math.floor((Math.random() * 475) + 1);


	/*
		for(var i=0; i <= snake.length; i++){
			snake[i] = snake_count;
			*/
		}
		//getting random x and y position
		 //rectRandX = Math.floor((Math.random() * 775) + 1);
		 //rectRandY = Math.floor((Math.random() * 475) + 1);
		 
	
}


/* //Or
	loadPixels();
 	var count_green;
 	count_green = checkColor(pixels,43);
	


 function checkColor(pixels,value){

 	var count_value = 0;
 	for(var l=0;l<=pixels.length;l++){
 		if(pixels[l]==value) 
 			count_value+=1;

 	}
 	return count_value;

 }

*/




	

