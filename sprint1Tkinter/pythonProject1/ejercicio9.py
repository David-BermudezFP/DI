import tkinter as tk
from tkinter import messagebox  # Importa el módulo messagebox para mostrar mensajes emergentes

# Crea la ventana principal de la aplicación
root = tk.Tk()
root.title("Ejercicio 9")
root.geometry("300x200")

# Función para la opción "Salir" en el menú
def salir():
    root.destroy()  # Cierra la ventana principal

# Función para la opción "Acerca de" en el menú
def mostrar_acerca_de():
    messagebox.showinfo("Acerca de", "Esta es una aplicación de ejemplo con menús.")  # Muestra un mensaje informativo

# Crear la barra de menú
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

# Menú "Archivo"
menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)  # Añade el menú "Archivo" a la barra de menú
menu_archivo.add_command(label="Abrir")  # Opción "Abrir" (sin funcionalidad)
menu_archivo.add_separator()  # Añade un separador
menu_archivo.add_command(label="Salir", command=salir)  # Opción "Salir"


# Menú "Ayuda"
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)  # Añade el menú "Ayuda" a la barra de menú
menu_ayuda.add_command(label="Acerca de", command=mostrar_acerca_de)  # Opción "Acerca de"


# Inicia el bucle principal de la interfaz gráfica
root.mainloop()
