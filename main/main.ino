#include <IRremote.h>
int red=2;
int green=3;
int blue=4;
int IR=11;


IRrecv irrecv(IR);
decode_results results;



void setup() {

  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  Serial.begin(9600);
  irrecv.enableIRIn();
  digitalWrite(red,1);
}


void loop() {

  String input;
  if (Serial.available() > 0) {
    input = Serial.readStringUntil('\n');
    if(input == "main"){
    digitalWrite(red,LOW);
    digitalWrite(blue, LOW);
    digitalWrite(green,HIGH);
    }
    if(input == "config"){
    digitalWrite(red,LOW);
    digitalWrite(blue,HIGH);
    }
}

  if (irrecv.decode(&results)){
      Serial.println(results.value);
      irrecv.resume();
      }
}
