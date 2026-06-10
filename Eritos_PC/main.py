import tkinter as tk

from Gato import Gato
from EritosUI import EritosUI
from BluetoothClient import BluetoothClient


root = tk.Tk()

bluetooth = BluetoothClient('COM6') ## cambiar COM? por el puerto al que se conecte 

gato = Gato(bluetooth)



ui = EritosUI(root, gato)

root.mainloop()



