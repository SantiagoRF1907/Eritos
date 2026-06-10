#ifndef SERVO_MOTOR_H
#define SERVO_MOTOR_H

#include <ESP32Servo.h>

class ServoMotor {
  private:
    int pin;
    Servo servo;

  public:
    ServoMotor(int p);
    void mover(int angulo);
};

#endif