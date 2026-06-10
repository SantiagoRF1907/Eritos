#ifndef MOVIMIENTO_CONTROLLER_H
#define MOVIMIENTO_CONTROLLER_H

#include "ServoMotor.h"

class MovimientoController {
  private:
    ServoMotor* servoMotores[4];
  
  public:
    MovimientoController();

    void agregarServo(int i, ServoMotor* s);

    void moverServo(int i, int angulo);
};

#endif