#include "ServoFactory.h"
#include "ServoMotor.h"

ServoMotor* ServoFactory::crearServo(int pin) {
  return new ServoMotor(pin);
}