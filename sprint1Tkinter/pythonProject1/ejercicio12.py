import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Crea la ventana principal de la aplicación
root = tk.Tk()
root.title("Ejercicio 12")
root.geometry("500x600")

# Variables globales
usuarios = []  # Lista para almacenar los usuarios registrados
nombre_var = tk.StringVar()  # Variable para el nombre del usuario
edad_var = tk.IntVar()  # Variable para la edad del usuario
genero_var = tk.StringVar(value="Masculino")  # Variable para el género (valor por defecto)

# Función para añadir usuario a la lista
def agregar_usuario():
    nombre = nombre_var.get()
    edad = edad_var.get()
    genero = genero_var.get()

    if nombre:  # Verifica que el campo nombre no esté vacío
        usuario = f"{nombre}, {edad}, {genero}" # Crea el usuario
        usuarios.append(usuario) # Añade el usuario
        lista_usuarios.insert(tk.END, usuario) # Inserta el usuario en el Listbox
        nombre_var.set("")  # Resetea el campo de nombre
        edad_var.set(0)  # Resetea el valor de edad
        genero_var.set("Masculino")  # Resetea el género por defecto
    else:
        messagebox.showwarning("Error", "El campo nombre no puede estar vacío")

# Función para eliminar el usuario seleccionado de la lista
def eliminar_usuario():
    seleccion = lista_usuarios.curselection()
    if seleccion:
        index = seleccion[0]
        lista_usuarios.delete(index)  # Elimina de la interfaz
        usuarios.pop(index)  # Elimina de la lista interna
    else:
        messagebox.showwarning("Error", "No se ha seleccionado ningún usuario")

# Función para guardar la lista de usuarios en un archivo
def guardar_lista():
    # Abre un cuadro de diálogo para guardar un archivo, dejando al usuario elegir la ubicación y el nombre del archivo.
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    # Si el usuario selecciona una ubicación y nombre de archivo (es decir, no cancela la operación)
    if file_path:
        # Abre el archivo en modo de escritura ("w")
        with open(file_path, "w") as file:
            # Itera sobre la lista de usuarios almacenada en la variable 'usuarios'
            for usuario in usuarios:
                # Escribe cada usuario en una nueva línea en el archivo
                file.write(usuario + "\n")
        # Muestra un cuadro de mensaje indicando que la lista se guardó con éxito
        messagebox.showinfo("Guardar Lista", "Lista guardada con éxito.")

# Función para cargar la lista de usuarios desde un archivo
def cargar_lista():
    # Abre un cuadro de diálogo para abrir un archivo, permitiendo al usuario seleccionar el archivo a cargar
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    # Si el usuario selecciona un archivo (no cancela la operación)
    if file_path:
        # Abre el archivo en modo de lectura ("r")
        with open(file_path, "r") as file:
            # Limpia el Listbox y la lista interna de usuarios
            lista_usuarios.delete(0, tk.END)
            usuarios.clear()

            # Lee el archivo línea por línea
            for line in file:
                # Quita los saltos de línea y espacios sobrantes con strip()
                usuario = line.strip()

                # Añade el usuario a la lista interna
                usuarios.append(usuario)

                # Inserta el usuario en el Listbox
                lista_usuarios.insert(tk.END, usuario)

        # Muestra un cuadro de mensaje indicando que la lista se cargó con éxito
        messagebox.showinfo("Cargar Lista", "Lista cargada con éxito.")


# Configura el menú de la aplicación
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Guardar Lista", command=guardar_lista)
menu_archivo.add_command(label="Cargar Lista", command=cargar_lista)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Etiquetas y entradas para nombre
tk.Label(root, text="Nombre:").pack(pady=5)
nombre_entry = tk.Entry(root, textvariable=nombre_var)
nombre_entry.pack(pady=5)

# Barra deslizante para seleccionar la edad
tk.Label(root, text="Edad:").pack(pady=5)
edad_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", variable=edad_var)
edad_scale.pack(pady=5)

# Botones de opción para seleccionar el género
tk.Label(root, text="Género:").pack(pady=5)
frame_genero = tk.Frame(root)
frame_genero.pack(pady=5)

tk.Radiobutton(frame_genero, text="Masculino", variable=genero_var, value="Masculino").pack(side="left", padx=5)
tk.Radiobutton(frame_genero, text="Femenino", variable=genero_var, value="Femenino").pack(side="left", padx=5)
tk.Radiobutton(frame_genero, text="Otro", variable=genero_var, value="Otro").pack(side="left", padx=5)

# Botón para añadir el usuario a la lista
boton_agregar = tk.Button(root, text="Añadir Usuario", command=agregar_usuario)
boton_agregar.pack(pady=10)

# Listbox para mostrar los usuarios registrados con Scrollbar
frame_lista = tk.Frame(root)
frame_lista.pack(pady=5, fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_lista, orient="vertical")
lista_usuarios = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_usuarios.yview)
scrollbar.pack(side="right", fill="y")
lista_usuarios.pack(side="left", fill="both", expand=True)

# Botón para eliminar el usuario seleccionado
boton_eliminar = tk.Button(root, text="Eliminar Usuario", command=eliminar_usuario)
boton_eliminar.pack(pady=5)

# Botón para cerrar la aplicación
boton_salir = tk.Button(root, text="Salir", command=root.quit)
boton_salir.pack(pady=5)

# Inicia el bucle principal de la interfaz gráfica
root.mainloop()
