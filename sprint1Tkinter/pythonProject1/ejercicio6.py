import tkinter  # Importa la biblioteca tkinter, que permite crear interfaces gráficas


root = tkinter.Tk()  # Crea la ventana principal de la aplicación
root.title("Ejercicio 6")  # Establece el título de la ventana
root.geometry("300x300") # Establece las dimensiones de la ventana principal

# Crear una lista de frutas
frutas = ["Manzana", "Banana", "Naranja"]

# Define la función para mostrar la fruta seleccionada
def mostrar_fruta():
    # Obtiene el índice de la fruta seleccionada en la lista
    seleccion = listbox.curselection()

    # Verifica si se seleccionó algún elemento
    if seleccion:
        fruta = listbox.get(seleccion)  # Obtiene el nombre de la fruta seleccionada
        label_resultado.config(text=f"Fruta seleccionada: {fruta}")  # Actualiza el texto de 'label_resultado'
    else:
        label_resultado.config(text="No has seleccionado ninguna fruta")  # Muestra un mensaje si no hay selección


# Crea un Listbox y añade elementos de frutas
listbox = tkinter.Listbox(root)
for fruta in frutas:
    listbox.insert(tkinter.END, fruta)  # Inserta la fruta en el Listbox
listbox.pack(pady=10)  # Posiciona el Listbox con un relleno vertical (pady) de 10 píxeles

# Crea un botón que ejecutará la función 'mostrar_fruta' al ser presionado
boton = tkinter.Button(root, text="Mostrar fruta seleccionada", command=mostrar_fruta)
boton.pack(pady=10)  # Posiciona el botón con un relleno vertical (pady) de 10 píxeles

# Crea una etiqueta para mostrar el nombre de la fruta seleccionada
label_resultado = tkinter.Label(root, text="Fruta seleccionada: ")
label_resultado.pack(pady=10)  # Posiciona la etiqueta con un relleno vertical (pady) de 10 píxeles

# Inicia el bucle principal de la interfaz gráfica
root.mainloop()