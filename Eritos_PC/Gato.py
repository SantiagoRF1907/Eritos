import time

class Gato:
    
    def __init__(self, bluetooth):
        self.bluetooth = bluetooth


    def mover_servo(
            self,
            servo,
            angulo
    ):
        comando = (
            f"S{servo}:{angulo}"
        )

        self.bluetooth.enviar(
            comando
        )


    def neutral(self):
        self.mover_servo(1,90)
        self.mover_servo(2,90)
        self.mover_servo(3,90)
        self.mover_servo(4,90)

    
    def avanzar(self):
        # Paso 1
        self.mover_servo(1,65)
        self.mover_servo(2,115)
        self.mover_servo(3,65)
        self.mover_servo(4,115)
        time.sleep(0.3)
        
        #Paso 2
        self.mover_servo(1,115)
        self.mover_servo(2,65)
        self.mover_servo(3,115)
        self.mover_servo(4,65)
        time.sleep(0.3)



    
    def sentarse(self):
        self.mover_servo(1,90)
        self.mover_servo(2,90)
        self.mover_servo(3,45)
        self.mover_servo(4,45)

