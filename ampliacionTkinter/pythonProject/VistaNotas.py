import tkinter as tk
from PIL import Image, ImageTk


class VistaNotas:
    def __init__(self, root):
        """
        Constructor de la clase VistaNotas.
        Inicializa la interfaz gráfica de la aplicación utilizando widgets de Tkinter.

        Parámetros:
        root (tk.Tk): La ventana raíz de la aplicación.
        """
        self.root = root
        self.root.title("Gestión de Notas")  # Título de la ventana principal

        # Etiqueta para el título de la aplicación
        self.label_titulo = tk.Label(root, text="Aplicación de Gestión de Notas", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        # Listbox para mostrar las notas
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        # Entry para ingresar una nueva nota
        self.entry_nota = tk.Entry(root, width=50)
        self.entry_nota.pack(pady=10)

        # Botones de la interfaz para las distintas funciones
        self.boton_agregar = tk.Button(root, text="Agregar Nota")  # Botón para agregar una nueva nota
        self.boton_eliminar = tk.Button(root, text="Eliminar Nota")  # Botón para eliminar la nota seleccionada
        self.boton_guardar = tk.Button(root, text="Guardar Notas")  # Botón para guardar las notas en un archivo
        self.boton_cargar = tk.Button(root, text="Cargar Notas")  # Botón para cargar notas desde un archivo
        self.boton_descargar = tk.Button(root, text="Descargar Imagen")  # Botón para descargar una imagen

        # Empaquetar los botones con espaciado
        self.boton_agregar.pack(pady=5)
        self.boton_eliminar.pack(pady=5)
        self.boton_guardar.pack(pady=5)
        self.boton_cargar.pack(pady=5)
        self.boton_descargar.pack(pady=5)

        # Etiqueta para mostrar las coordenadas del clic del ratón
        self.label_coordenadas = tk.Label(root, text="Coordenadas del clic:")
        self.label_coordenadas.pack(pady=10)

        # Etiqueta para mostrar la imagen descargada
        self.label_imagen = tk.Label(root)
        self.label_imagen.pack(pady=10)

        # Vincular el evento de clic izquierdo en la ventana para actualizar coordenadas
        self.root.bind("<Button-1>", self.actualizar_coordenadas)

    def actualizar_coordenadas(self, event):
        """
        Actualiza la etiqueta de coordenadas para mostrar la posición del clic del ratón.

        Parámetros:
        event (tk.Event): El evento de clic que contiene las coordenadas x e y.
        """
        self.label_coordenadas.config(text=f"Coordenadas: ({event.x}, {event.y})")

    def actualizar_listbox(self, notas):
        """
        Actualiza el Listbox para mostrar la lista de notas actuales.

        Parámetros:
        notas (list): Lista de notas a mostrar en el Listbox.
        """
        self.listbox.delete(0, tk.END)  # Limpiar el Listbox actual
        for nota in notas:  # Insertar cada nota en el Listbox
            self.listbox.insert(tk.END, nota)

    def mostrar_imagen(self, ruta_imagen):
        """
        Muestra una imagen en el Label de imagen después de descargarla y ajustarla de tamaño.

        Parámetros:
        ruta_imagen (str): La ruta local donde se guarda la imagen descargada.
        """
        # Cargar y redimensionar la imagen para ajustarla al tamaño del label
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((200, 200))  # Ajustar el tamaño de la imagen
        self.imagen_tk = ImageTk.PhotoImage(imagen)  # Convertir la imagen a un formato compatible con Tkinter

        # Mostrar la imagen en el Label de imagen
        self.label_imagen.config(image=self.imagen_tk)
        self.label_imagen.image = self.imagen_tk  # Mantener una referencia a la imagen para evitar que sea eliminada por el recolector de basura