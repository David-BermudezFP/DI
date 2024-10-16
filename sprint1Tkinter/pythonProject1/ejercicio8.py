import tkinter as tk  # Importa la biblioteca tkinter

# Crea la ventana principal de la aplicación
root = tk.Tk()
root.title("Ejercicio 8")

# Establece las dimensiones de la ventana
root.geometry("300x400")

# Frame superior
frame_superior = tk.Frame(root, bd="2", bg="lightgrey")
frame_superior.pack(pady=10, padx=10, fill="both", expand=True)  # Coloca el frame superior con relleno vertical

# Etiquetas y campo de entrada en el Frame superior
label1 = tk.Label(frame_superior, text="Etiqueta 1")
label1.pack(padx=5, pady=5)

label2 = tk.Label(frame_superior, text="Etiqueta 2")
label2.pack(padx=5, pady=5)

entry = tk.Entry(frame_superior, width=25)
entry.pack(padx=5, pady=5)  # Abarca ambas columnas

# Frame inferior
frame_inferior = tk.Frame(root, bd="2", bg="lightgrey")
frame_inferior.pack(pady=10, padx=10, fill="both", expand=True)  # Coloca el frame inferior con relleno vertical

# Función para mostrar el contenido del Entry en una etiqueta
def mostrar_contenido():
    contenido = entry.get()  # Obtiene el contenido del Entry
    label_resultado.config(text=f"Contenido: {contenido}")

# Función para borrar el contenido del Entry
def borrar_contenido():
    entry.delete(0, tk.END)  # Borra el contenido del Entry
    label_resultado.config(text="")  # Actualiza la etiqueta de resultado

# Botones en el Frame inferior
boton_mostrar = tk.Button(frame_inferior, text="Mostrar", command=mostrar_contenido)
boton_mostrar.pack(pady=10, padx=10)

boton_borrar = tk.Button(frame_inferior, text="Borrar", command=borrar_contenido)
boton_borrar.pack(pady=10, padx=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

# Inicia el bucle principal de la interfaz gráfica
root.mainloop()
