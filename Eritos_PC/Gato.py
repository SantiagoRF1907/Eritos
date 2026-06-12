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
        self.mover_servo(4,90)
        self.mover_servo(3,90)
        time.sleep(0.3)
        self.mover_servo(1,90)
        self.mover_servo(2,90)
        

    
    def caminar(self):
        
        # Paso 1
        self.mover_servo(1,40) # Servo 1 y 4 adelante
        self.mover_servo(4,140)
        time.sleep(0.5)
        self.mover_servo(2,40) # Servo 2 y 3 atras
        self.mover_servo(3,140)
        time.sleep(0.5)

        # Paso intermedio -- Todos neutral
        self.neutral()

        # Paso 2
        self.mover_servo(2,140) # Servo 2 y 3 adelante
        self.mover_servo(3,40)
        time.sleep(0.5)
        self.mover_servo(1,140) # Servo 1 y 4 atras
        self.mover_servo(4,40)
        
        self.neutral()


    def sentarse(self):
        self.mover_servo(1,90)
        self.mover_servo(2,90)
        time.sleep(0.3)
        self.mover_servo(3,30)
        self.mover_servo(4,150)


    def darLaPata(self):
        for i in range(5):
            self.mover_servo(2,180)
            time.sleep(0.2)
            self.mover_servo(2,130)
            time.sleep(0.2)
        self.mover_servo(2,90) 