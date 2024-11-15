import tkinter as tk
from controlador import GameController

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200")  # Tamaño de la ventana

    # Inicializar el controlador
    controller = GameController(root)

    # Ejecutar la aplicación
    root.mainloop()