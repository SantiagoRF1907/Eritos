import serial
import time

class BluetoothClient:

    def __init__(self, puerto, velocidad=115200):

        print("Intentando abrir", puerto)

        self.serial = serial.Serial(
            puerto,
            velocidad,
            timeout=1
        )

        print("Puerto abierto")

        time.sleep(2)

        print("Bluetooth listo")

    def enviar(self, mensaje):
        self.serial.write(
            f"{mensaje}\n".encode()
        )
    
    def cerrar(self):
        self.serial.close()