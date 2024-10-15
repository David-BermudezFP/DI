import tkinter  # Importa la biblioteca tkinter, que permite crear interfaces gráficas

# Crea la ventana principal de la aplicación
root = tkinter.Tk()
root.title("Ejercicio 4")  # Establece el título de la ventana

# Establece las dimensiones de la ventana principal
root.geometry("300x150")

# Variables asociadas a las casillas de verificación
aficion_leer = tkinter.BooleanVar()  # Variable para la afición "Leer"
aficion_deporte = tkinter.BooleanVar()  # Variable para la afición "Deporte"
aficion_musica = tkinter.BooleanVar()  # Variable para la afición "Música"

# Función que actualiza el estado de las aficiones seleccionadas
def actualizar_aficiones():
    seleccion = "Aficiones seleccionadas: "
    if aficion_leer.get():
        seleccion += "Leer "
    if aficion_deporte.get():
        seleccion += "Deporte "
    if aficion_musica.get():
        seleccion += "Música"
    label_resultado.config(text=seleccion)  # Actualiza el texto de 'label_resultado'

# Creación de las casillas de verificación para cada afición
check_leer = tkinter.Checkbutton(root, text="Leer", variable=aficion_leer, command=actualizar_aficiones)
check_leer.pack(anchor="nw")  # Coloca la casilla alineada arriba a la izquierda

check_deporte = tkinter.Checkbutton(root, text="Deporte", variable=aficion_deporte, command=actualizar_aficiones)
check_deporte.pack(anchor="nw")  # Coloca la casilla alineada arriba a la izquierda

check_musica = tkinter.Checkbutton(root, text="Música", variable=aficion_musica, command=actualizar_aficiones)
check_musica.pack(anchor="nw")  # Coloca la casilla alineada arriba a la izquierda

# Etiqueta para mostrar las aficiones seleccionadas
label_resultado = tkinter.Label(root, text="Aficiones seleccionadas:")
label_resultado.pack(pady=10)  # Aplica un relleno vertical (pady) de 10 píxeles

# Inicia el bucle principal de la interfaz gráfica
root.mainloop()