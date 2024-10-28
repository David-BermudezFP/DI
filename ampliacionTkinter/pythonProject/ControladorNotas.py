import threading
import requests
from tkinter import messagebox
import tkinter as tk  # Importar tkinter correctamente para el manejo de END y otros métodos


class ControladorNotas:
    def __init__(self, vista, modelo):
        """
        Constructor de la clase ControladorNotas.
        Establece la conexión entre la vista y el modelo, y asigna comandos a los botones de la vista.

        Parámetros:
        vista (VistaNotas): La instancia de la clase VistaNotas que maneja la interfaz gráfica.
        modelo (NotasModel): La instancia de la clase NotasModel que maneja la lógica de las notas.
        """
        self.vista = vista
        self.modelo = modelo

        # Asignar funciones de controlador a cada botón de la vista
        self.vista.boton_agregar.config(command=self.agregar_nota)
        self.vista.boton_eliminar.config(command=self.eliminar_nota)
        self.vista.boton_guardar.config(command=self.guardar_notas)
        self.vista.boton_cargar.config(command=self.cargar_notas)
        self.vista.boton_descargar.config(command=self.descargar_imagen)

    def agregar_nota(self):
        """
        Obtiene la nueva nota desde el Entry de la vista y la añade al modelo.
        Luego, actualiza el Listbox con las notas actuales y limpia el Entry.
        """
        nueva_nota = self.vista.entry_nota.get()  # Obtener el texto del Entry
        if nueva_nota:  # Verificar que el texto no esté vacío
            self.modelo.agregar_nota(nueva_nota)  # Agregar la nota al modelo
            self.vista.actualizar_listbox(self.modelo.obtener_notas())  # Actualizar el Listbox con las notas actuales
            self.vista.entry_nota.delete(0, tk.END)  # Limpiar el Entry después de agregar la nota

    def eliminar_nota(self):
        """
        Elimina la nota seleccionada en el Listbox y actualiza la lista.
        """
        indice = self.vista.listbox.curselection()  # Obtener el índice de la nota seleccionada en el Listbox
        if indice:  # Verificar que haya una nota seleccionada
            self.modelo.eliminar_nota(indice[0])  # Eliminar la nota en el índice seleccionado
            self.vista.actualizar_listbox(self.modelo.obtener_notas())  # Actualizar el Listbox con las notas restantes

    def guardar_notas(self):
        """
        Guarda todas las notas actuales en un archivo de texto llamando al método del modelo
        y muestra un mensaje de confirmación.
        """
        self.modelo.guardar_notas()  # Guardar las notas en el archivo
        messagebox.showinfo("Guardar Notas", "Notas guardadas correctamente.")  # Mostrar mensaje de confirmación

    def cargar_notas(self):
        """
        Carga las notas desde el archivo de texto y actualiza la lista en la vista.
        """
        self.modelo.cargar_notas()  # Cargar las notas desde el archivo
        self.vista.actualizar_listbox(self.modelo.obtener_notas())  # Actualizar el Listbox con las notas cargadas

    def descargar_imagen(self):
        """
        Descarga una imagen desde una URL utilizando un hilo separado para evitar
        bloquear la interfaz gráfica durante la descarga.
        """
        url = "https://static.wikia.nocookie.net/villains/images/5/57/Red_Soldier.png/revision/latest?cb=20200430130617"
        # Iniciar un nuevo hilo para descargar la imagen sin congelar la interfaz gráfica
        threading.Thread(target=self._descargar_imagen, args=(url,)).start()

    def _descargar_imagen(self, url):
        """
        Método auxiliar que realiza la descarga de la imagen.
        Descarga la imagen desde la URL proporcionada y la guarda en la ruta especificada,
        luego actualiza la vista para mostrar la imagen descargada.

        Parámetros:
        url (str): La URL desde donde se descargará la imagen.
        """
        response = requests.get(url)  # Realizar la solicitud HTTP para descargar la imagen
        ruta_imagen = 'imagen_descargada.png'  # Especificar la ruta de guardado de la imagen
        with open(ruta_imagen, 'wb') as f:
            f.write(response.content)  # Guardar el contenido de la imagen en un archivo local
        self.vista.mostrar_imagen(ruta_imagen)  # Mostrar la imagen en la vista después de descargarla