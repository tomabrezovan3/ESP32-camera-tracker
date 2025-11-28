#include <Arduino.h>
#include <Servo.h>

Servo servoX;
Servo servoY;

void setup() {
  Serial.begin(115200);
  servoX.attach(4);  // example pins
  servoY.attach(5);
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');
    // expected: "x:100,y:50"
    Serial.println("Received: " + data);
  }

  delay(10);
}
