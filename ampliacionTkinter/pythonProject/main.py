import tkinter as tk
from NotasModel import NotasModel
from VistaNotas import VistaNotas
from ControladorNotas import ControladorNotas

# Ejecutar la aplicación solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    # Crear la ventana principal de Tkinter
    root = tk.Tk()

    # Instanciar el modelo de notas que maneja los datos de la aplicación
    modelo = NotasModel()

    # Crear la vista que define la interfaz gráfica de usuario, pasando la ventana raíz
    vista = VistaNotas(root)

    # Instanciar el controlador, conectando la vista y el modelo para manejar la lógica de la aplicación
    controlador = ControladorNotas(vista, modelo)

    # Iniciar el bucle principal de la interfaz gráfica
    root.mainloop()