#ifndef BLUETOOTH_MANAGER_H
#define BLUETOOTH_MANAGER_H

#include <BluetoothSerial.h>

class BluetoothManager {
  private:
    BluetoothSerial bluetooth;
  
  public:
    void iniciar();
    
    bool disponible();

    String leerComando();
};

#endif