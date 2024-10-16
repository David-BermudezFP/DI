import tkinter  # Importa la biblioteca tkinter, que permite crear interfaces gráficas

root = tkinter.Tk()  # Crea la ventana principal de la aplicación
root.title("Ejercicio 7")  # Establece el título de la ventana
root.geometry("400x550") # Establece las dimensiones de la ventana principal

# Crea un Canvas en la ventana
canvas = tkinter.Canvas(root, width=300, height=300, bg="white")
canvas.pack(pady=20)

# Etiquetas y campos de entrada para las coordenadas y tamaños

# Coordenadas y tamaño para el círculo
label_circle = tkinter.Label(root, text="Círculo - Coordenada X, Y, Radio:")
label_circle.pack()
entry_circle = tkinter.Entry(root)
entry_circle.pack()

# Coordenadas y tamaño para el rectángulo
label_rectangle = tkinter.Label(root, text="Rectángulo - Coordenada X1, Y1, X2, Y2:")
label_rectangle.pack()
entry_rectangle = tkinter.Entry(root)
entry_rectangle.pack()


# Función para dibujar un círculo con las coordenadas y radio ingresados
def dibujar_circulo():
    try:
        # Obtiene las coordenadas y el radio del campo de entrada
        x, y, r = map(int, entry_circle.get().split(","))

        # Dibuja el círculo en el Canvas
        # Como se pasan los datos como a un ovalo se les suma o resta el radio para tener los 4 puntos
        canvas.create_oval(x - r, y - r, x + r, y + r, outline="blue", fill="lightblue")
        label_error.configure(text="")
    except ValueError:
        label_error.configure(text="Por favor, ingresa coordenadas y radio válidos para el círculo.")


# Función para dibujar un rectángulo con las coordenadas ingresadas
def dibujar_rectangulo():
    try:
        # Obtiene las coordenadas del campo de entrada
        x1, y1, x2, y2 = map(int, entry_rectangle.get().split(","))

        # Dibuja el rectángulo en el Canvas
        canvas.create_rectangle(x1, y1, x2, y2, outline="green", fill="lightgreen")
        label_error.configure(text="")
    except ValueError:
        label_error.configure(text="Por favor, ingresa coordenadas válidas para el rectángulo.")


# Botones para dibujar las figuras
boton_circulo = tkinter.Button(root, text="Dibujar Círculo", command=dibujar_circulo)
boton_circulo.pack(pady=5)

boton_rectangulo = tkinter.Button(root, text="Dibujar Rectángulo", command=dibujar_rectangulo)
boton_rectangulo.pack(pady=5)

# Label que solo se mostrará en caso de haber error con los datos
label_error = tkinter.Label(root, text="", fg="red")
label_error.pack(pady=5)

# Inicia el bucle principal de la interfaz gráfica
root.mainloop()