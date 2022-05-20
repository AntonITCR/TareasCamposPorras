//Programado y modificado por David Portilla
//
//Para más proyectos y cursos, entra en https://codiziapp.com/
#include <Servo.h>
Servo servo1;

int pinServo = 9;
String inString = "";

void setup() {
  Serial.begin(9600);
  servo1.attach(pinServo);
}

void loop() {
  if(Serial.available() > 0){
    int inChar = Serial.read();
    if(inChar != '\n'){
      inString += (char)inChar; 
    }else{
      float angulo =inString.toFloat();
      Serial.println(angulo);
      servo1.write(angulo);
      inString = "";
    }
  }
}
