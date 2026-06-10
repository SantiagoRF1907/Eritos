#ifndef SERVO_FACTORY_H 
#define SERVO_FACTORY_H 

#include "ServoMotor.h"

class ServoFactory {
  public:
    static ServoMotor* crearServo(int pin);
};

#endif
