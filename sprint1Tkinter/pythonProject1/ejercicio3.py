import tkinter  # Importa la biblioteca tkinter, que permite crear interfaces gráficas

# Crea la ventana principal de la aplicación
root = tkinter.Tk()
root.title("Ejercicio 3")  # Establece el título de la ventana

# Establece las dimensiones de la ventana principal a 300 píxeles de ancho por 150 píxeles de alto
root.geometry("300x150")

# Define una función para mostrar un saludo personalizado con el nombre ingresado
def mostrar_saludo():
    nombre = entry.get()  # Obtiene el texto del campo de entrada
    saludo = f"¡Hola, {nombre}!"  # Crea un mensaje de saludo personalizado
    label2.config(text=saludo)  # Actualiza el texto de 'label_saludo' con el mensaje

# Crea un label con el texto "Ingresa tu nombre:" y lo coloca en la ventana
label1 = tkinter.Label(root, text="Ingresa tu nombre:")
label1.pack(pady=5)  # Usa pack() para posicionar el label y aplica un relleno vertical (pady) de 5 píxeles

# Crea un campo de entrada para que el usuario pueda escribir su nombre
entry = tkinter.Entry(root)
entry.pack(pady=5)  # Usa pack() para posicionar el campo de entrada y aplica un relleno vertical (pady) de 5 píxeles

# Crea un botón que ejecutará la función 'mostrar_saludo' al ser presionado
boton = tkinter.Button(root, text="Mostrar saludo", command=mostrar_saludo)
boton.pack(pady=5)  # Usa pack() para posicionar el botón y aplica un relleno vertical (pady) de 5 píxeles

# Crea una etiqueta que inicialmente estará vacía y se actualizará con el saludo personalizado
label2 = tkinter.Label(root, text="")
label2.pack(pady=5)  # Usa pack() para posicionar el label y aplica un relleno vertical (pady) de 5 píxeles

# Inicia el bucle principal de la interfaz gráfica, permitiendo que la ventana se muestre y funcione
root.mainloop()
