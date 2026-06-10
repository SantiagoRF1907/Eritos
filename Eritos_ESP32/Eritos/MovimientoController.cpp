#include "MovimientoController.h"
#include <Arduino.h>

MovimientoController::MovimientoController() {
  for(int i = 0; i < 4; i++) {
    servoMotores[i] = nullptr;
  }
}

void MovimientoController::agregarServo(int i, ServoMotor* s) {
  servoMotores[i] = s;
}

void MovimientoController::moverServo(int i, int angulo) {
  if(servoMotores[i] != nullptr) {
    servoMotores[i]->mover(angulo);
  }
}