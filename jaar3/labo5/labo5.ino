#include <Wire.h>

#define potPin A0
byte analogVal = 0;

void setup() { 
  Wire.begin(0x14);
  Wire.onRequest(requestEvent);
}

void loop() {
  analogVal = analogRead(potPin);
  delay(100);
}

void requestEvent(){
  Wire.write(analogVal);
}

