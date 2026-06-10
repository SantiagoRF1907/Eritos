// Librerias
#include "ServoMotor.h"
#include "ServoFactory.h"
#include "MovimientoController.h"
#include "BluetoothManager.h"


MovimientoController* movimiento;
BluetoothManager bluetooth;
ServoMotor* servos[4];


// Declaracion 
void procesarComando(String comando);


void setup() {
    Serial.begin(115200);

    bluetooth.iniciar();

    // Crear movimiento
    movimiento = new MovimientoController;

    // Crear Motores
    servos[0] = ServoFactory::crearServo(13);
    servos[1] = ServoFactory::crearServo(12);
    servos[2] = ServoFactory::crearServo(25);
    servos[3] = ServoFactory::crearServo(32);

    for(int i = 0; i < 4; i++) {
      movimiento->agregarServo(i, servos[i]);
    }
}


void loop() {  

  if(bluetooth.disponible()){

    String comando = bluetooth.leerComando();

    procesarComando(comando);
  }
}


// Implementacion
void procesarComando(String comando) {

  comando.trim();
  

  int separador = comando.indexOf(':');
  // Validar formato
  if(separador == -1 || comando.charAt(0) != 'S') {
    Serial.println("Formato invalido");
    return;
  }

  int servo = comando.substring(1, separador).toInt();

  int angulo = comando.substring(separador + 1).toInt();


  Serial.print("Servo: ");
  Serial.println(servo);

  Serial.print("Angulo: ");
  Serial.println(angulo);

  if(servo >= 1 && servo <= 4 && angulo >= 0 && angulo <= 180) {
    movimiento->moverServo(servo - 1, angulo);
  }
  else {
    Serial.println("Comando invalido");
  }
}
