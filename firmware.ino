#include "M5Atom.h"
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPU6050 mpu;
const int motorPin = 22;

void setup() {
  M5.begin(true, false, true); // Serial, I2C, Display
  if (!mpu.begin()) { while (1); }
  pinMode(motorPin, OUTPUT);
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  // Calculate Pitch (Angle from vertical)
  float pitch = atan2(-a.acceleration.x, sqrt(a.acceleration.y * a.acceleration.y + a.acceleration.z * a.acceleration.z)) * 180 / PI;

  if (pitch > 20.0) { // Slouching detected
    digitalWrite(motorPin, HIGH); 
    M5.dis.drawpix(0, 0xff0000); // Red LED
  } else {
    digitalWrite(motorPin, LOW);
    M5.dis.drawpix(0, 0x00ff00); // Green LED
  }
  
  // JSON Broadcast logic via WiFi...
  delay(500);
}
