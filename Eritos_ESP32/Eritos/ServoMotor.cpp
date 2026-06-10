#include "ServoMotor.h"
#include <Arduino.h>

ServoMotor::ServoMotor(int p) : pin(p) {
  servo.setPeriodHertz(50);
  servo.attach(p, 500, 2400);
}

void ServoMotor::mover(int angulo) {
  servo.write(angulo);
}