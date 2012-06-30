// Sweep
// by BARRAGAN <http://barraganstudio.com> 
// This example code is in the public domain.


#include <Servo.h> 
#include <SoftwareSerial.h>
 
SoftwareSerial mySerial(2, 3); // RX, TX

Servo myservo1;
Servo myservo2; 

int val = 0;
int ser = 0;
 
void setup() 
{ 
  myservo1.attach(6);
  myservo2.attach(5);
  Serial.begin(9600);
} 
 
 
void loop() 
{ 
  while(!Serial.available()){
    delay(50);
  }
  ser = Serial.read();
  val = Serial.read();
  Serial.flush();
  //val = map(val, 0, 100, 0, 179);
  //Movemos el servo indicado en el valor indicado
  switch(ser){
    case 1:
      myservo1.write(val);
      break;
    case 2:
      myservo2.write(val);
      break;
  }
  Serial.println(val);
} 
