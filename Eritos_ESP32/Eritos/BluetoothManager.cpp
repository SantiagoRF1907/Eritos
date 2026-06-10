#include "BluetoothManager.h"

void BluetoothManager::iniciar() {
  bluetooth.begin("Eritos", true);
}

bool BluetoothManager::disponible() {
  return bluetooth.available();
}

String BluetoothManager::leerComando() {
  return bluetooth.readStringUntil('\n');
}