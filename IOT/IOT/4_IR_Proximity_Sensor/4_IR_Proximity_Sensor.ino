const int pin = 7; //LED connected to this pin
const int ir = 4; //Out of IR is connected to this PIN
void setup() {
  // put your setup code here, to run once:
  pinMode(pin,OUTPUT);
  pinMode(ir,INPUT); //We are going to take the input from IR sensor
}

void loop() {
  // put your main code here, to run repeatedly:
  // To read from IR
  int val = digitalRead(ir);
  if(val == LOW){
    // if(val == 0) also can be used
    digitalWrite(pin,HIGH);
    delay(1000);  
  }else{
    digitalWrite(pin,LOW);  
    delay(1000);  
  }
}
