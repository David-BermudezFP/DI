import tkinter  # Importa la biblioteca tkinter, que permite crear interfaces gráficas

# Crea la ventana principal de la aplicación
root = tkinter.Tk()
root.title("Ejercicio 2")  # Establece el título de la ventana

# Establece las dimensiones de la ventana principal a 300 píxeles de ancho por 150 píxeles de alto
root.geometry("300x150")

# Define una función que cambiará el texto de 'label1' cuando se llame
def mostrar_mensaje():
    label1.config(text="HOLA ESTABA ESCONDIDO")  # Cambia el texto de 'label1' a un mensaje específico

# Crea un label (etiqueta) vacío, que se actualizará al presionar el botón
label1 = tkinter.Label(root, text="")
label1.pack(pady=30)  # Usa pack() para posicionar el label y aplica un relleno vertical (pady) de 30 píxeles

# Crea un botón que ejecutará 'mostrar_mensaje' para cambiar el texto de 'label1' al ser presionado
boton1 = tkinter.Button(root, text="Mostrar mensaje", command=mostrar_mensaje)
boton1.place(x=10, y=120)  # Usa place() para posicionar el botón en coordenadas (10, 120)

# Crea un segundo botón que cerrará la ventana principal al ser presionado
boton2 = tkinter.Button(root, text="Cerrar ventana", command=root.destroy)
boton2.place(x=200, y=120)  # Usa place() para posicionar este botón en coordenadas (200, 120)

# Inicia el bucle principal de la interfaz gráfica, permitiendo que la ventana se muestre y funcione
root.mainloop()
