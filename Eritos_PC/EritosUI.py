import tkinter as tk

class EritosUI:

    def __init__(self, root, gato):
        
        self.root = root

        self.gato = gato

        self.root.title("Eritos")

        self.contador = 0


        # Contador de pasos

        self.labelPasos = tk.Label(
            root,
            text = "Pasos: 0"
        )

        self.labelPasos.pack()


        # Botones

        self.btnCaminar = tk.Button(
            root,
            text = "Caminar",
            command = self.caminar
        )

        self.btnCaminar.pack()


        self.btnNeutral = tk.Button(
            root,
            text = "Neutral",
            command = self.neutral
        )

        self.btnNeutral.pack()


        self.btnSentarse = tk.Button(
            root,
            text = "Sentarse",
            command = self.sentarse
        )

        self.btnSentarse.pack()


        self.btnDarLaPata = tk.Button(
            root,
            text = "Saludar",
            command = self.darLaPata
        )

        self.btnDarLaPata.pack()


        # Consola

        self.log = tk.Text(
            root,
            width = 50,
            height = 15
        )

        self.log.pack()

    
    # Metodos

    def agregarLog(self, texto):

        self.log.insert(
            tk.END,
            texto + "\n"
        )

        self.log.see(tk.END)
    

    def actualizarPasos(self):

        self.contador += 1

        self.labelPasos.config(
            text = f"Pasos: {self.contador}"
        )


    def caminar(self):

        self.gato.caminar()

        self.actualizarPasos()

        self.agregarLog("Comando: Caminar")
    
    
    def neutral(self):

        self.gato.neutral()

        self.agregarLog("Comando: Neutral")

    
    def sentarse(self):

        self.gato.sentarse()

        self.agregarLog("Comando: Sentarse")


    def darLaPata(self):

        self.gato.darLaPata()

        self.agregarLog("Comando: Dar la pata")
