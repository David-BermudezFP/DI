import tkinter  # Importa la biblioteca tkinter, que permite crear interfaces gráficas

# Crea la ventana principal de la aplicación
root = tkinter.Tk()
root.title("Ejercicio 1")  # Establece el título de la ventana

# Establece las dimensiones de la ventana principal a 300 píxeles de ancho por 150 píxeles de alto
root.geometry("300x150")

# Define una función que cambiará el texto de 'label3' al hacer clic en el botón
def cambiar_label():
    label3["text"] = "Encantado de conocerte, David!"  # Cambia el texto de 'label3'
    boton1.destroy()  # Destruye el boton para que no se pueda volver a pulsar ya que no tiene mas usos

# Crea un label (etiqueta) con un mensaje de bienvenida y lo agrega a la ventana
label1 = tkinter.Label(root, text="Hola bienvenido!")
label1.pack()  # Usa pack() para posicionar el label automáticamente

# Crea un segundo label con un mensaje que indica el nombre del creador
label2 = tkinter.Label(root, text="Mi nombre es David")
label2.pack()  # Usa pack() para posicionar el label automáticamente

# Crea un tercer label con un mensaje que se actualizará cuando se haga clic en el botón
label3 = tkinter.Label(root, text="*Tu respuesta*", bg="lightgray")
label3.pack(pady=15)  # Usa pack() para posicionar el label automáticamente

# Crea un botón con el texto "Saludar" que, al hacer clic, ejecutará la función 'cambiar_label'
boton1 = tkinter.Button(root, text="Saludar", command=cambiar_label)
boton1.pack(pady=20)  # Usa pack() para posicionar el botón automáticamente

# Inicia el bucle principal de la interfaz gráfica, permitiendo que la ventana se muestre y funcione
root.mainloop()