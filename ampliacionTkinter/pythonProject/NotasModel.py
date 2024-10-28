import os

class NotasModel:
    def __init__(self):
        """
        Constructor de la clase NotasModel.
        Inicializa una lista vacía para almacenar las notas y carga las notas
        existentes desde el archivo 'notas.txt', si el archivo existe.
        """
        self.notas = []
        self.cargar_notas()

    def agregar_nota(self, nueva_nota):
        """
        Agrega una nueva nota a la lista de notas.

        Parámetros:
        nueva_nota (str): El texto de la nueva nota a agregar.
        """
        self.notas.append(nueva_nota)

    def eliminar_nota(self, indice):
        """
        Elimina una nota en el índice especificado de la lista de notas.

        Parámetros:
        indice (int): El índice de la nota a eliminar.
        """
        del self.notas[indice]

    def obtener_notas(self):
        """
        Devuelve la lista de notas.

        Devuelve:
        list: La lista de notas.
        """
        return self.notas

    def guardar_notas(self):
        """
        Guarda todas las notas actuales en un archivo de texto llamado 'notas.txt'.
        Cada nota se guarda en una nueva línea dentro del archivo.
        """
        with open('notas.txt', 'w') as f:
            for nota in self.notas:
                f.write(nota + '\n')

    def cargar_notas(self):
        """
        Carga las notas desde el archivo 'notas.txt' y las almacena en la lista
        de notas. Si el archivo no existe, no realiza ninguna acción.
        """
        if os.path.exists('notas.txt'):
            with open('notas.txt', 'r') as f:
                # Lee cada línea, elimina saltos de línea y la añade a la lista de notas.
                self.notas = [line.strip() for line in f.readlines()]