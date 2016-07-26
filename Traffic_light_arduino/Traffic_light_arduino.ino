/* Program Discription:
 *  Authors:Nana,Kevin,Deangelo
 *  Breief:
 *  Date:
 *  Revision: 
 * */


//Defining the LED pins
int RedLED = 12;
int YellowLED = 11;
int GreenLED = 10;
int RedLEDSecond = 9;
int YellowLED2 = 8;
const int Button = 2; //This is at pin 2
int CarGo = GreenLED;
int CarCaution = YellowLED;
int CarStop = RedLED;
int PedGo = YellowLED2;
int PedStop = RedLEDSecond;
int buttonState = 0;
//Setup the pins to output and input
void setup() {
  pinMode(RedLED,OUTPUT);
  pinMode(YellowLED,OUTPUT);
  pinMode(GreenLED,OUTPUT);
  pinMode(RedLEDSecond,OUTPUT);
  pinMode(YellowLED2,OUTPUT);
  pinMode(Button,INPUT);
  digitalWrite(GreenLED,HIGH);
  digitalWrite(RedLEDSecond,HIGH);


}

void loop() {
  
  buttonState = digitalRead(Button);

  if(buttonState == HIGH) {
    digitalWrite(GreenLED,LOW);
    digitalWrite(YellowLED,HIGH);
    delay(2000);
    digitalWrite(YellowLED,LOW);
    digitalWrite(RedLED,HIGH);
    delay(1000);
    digitalWrite(RedLEDSecond,LOW);
    digitalWrite(PedGo,HIGH);
    int i = 0;
    while(YellowLED2,HIGH and i != 21) {
      digitalWrite(YellowLED2,HIGH);
      delay(250);
      digitalWrite(YellowLED2,LOW);
      delay(250);
      i++;
    }
    digitalWrite(YellowLED2,HIGH);
    digitalWrite(YellowLED2,LOW);
    digitalWrite(RedLEDSecond,HIGH);
    delay(1000);
    digitalWrite(RedLED,LOW);
    digitalWrite(GreenLED,HIGH);
    
  }
    


}
