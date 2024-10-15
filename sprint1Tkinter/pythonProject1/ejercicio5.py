import tkinter  # Importa la biblioteca tkinter, que permite crear interfaces gráficas

# Crea la ventana principal de la aplicación
root = tkinter.Tk()
root.title("Ejercicio 5")  # Establece el título de la ventana

# Establece las dimensiones de la ventana principal
root.geometry("300x150")

# Variable para almacenar el color seleccionado
color_seleccionado = tkinter.StringVar()
color_seleccionado.set("Blanco")  # Color inicial de fondo


# Función que cambia el color de fondo según el color seleccionado
def cambiar_color():
    color = color_seleccionado.get()  # Obtiene el valor del color seleccionado
    root.configure(bg=color)  # Cambia el color de fondo de la ventana


# Creación de los botones de opción para cada color
radiobutton_rojo = tkinter.Radiobutton(root, text="Rojo", variable=color_seleccionado, value="red",
                                       command=cambiar_color)
radiobutton_rojo.pack(anchor="w")  # Coloca el botón alineado a la izquierda

radiobutton_verde = tkinter.Radiobutton(root, text="Verde", variable=color_seleccionado, value="green",
                                        command=cambiar_color)
radiobutton_verde.pack(anchor="w")  # Coloca el botón alineado a la izquierda

radiobutton_azul = tkinter.Radiobutton(root, text="Azul", variable=color_seleccionado, value="blue",
                                       command=cambiar_color)
radiobutton_azul.pack(anchor="w")  # Coloca el botón alineado a la izquierda

# Inicia el bucle principal de la interfaz gráfica
root.mainloop()
