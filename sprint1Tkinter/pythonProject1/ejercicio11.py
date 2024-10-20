import tkinter as tk

# Crea la ventana principal de la aplicación
root = tk.Tk()
root.title("Ejercicio 11")
root.geometry("300x150")

# Función que actualiza la etiqueta con el valor seleccionado
def actualizar_valor(valor):
    label.config(text=f"Valor seleccionado: {valor}")

# Crea una barra deslizante (Scale) con un rango de 0 a 100
scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar_valor)
scale.pack(pady=20)

# Crea una etiqueta para mostrar el valor seleccionado
label = tk.Label(root, text="Valor seleccionado: 0")
label.pack()

# Inicia el bucle principal de la interfaz gráfica
root.mainloop()