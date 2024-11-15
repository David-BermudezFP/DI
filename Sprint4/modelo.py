import threading
import time
import random
import datetime
from recursos import descargar_imagen


class GameModel:
    def __init__(self, difficulty, player_name, cell_size= 100):
        # Inicialización de los atributos del juego
        self.difficulty = difficulty
        self.player_name = player_name
        self.cell_size = cell_size
        self.tablero = []
        self.start_time = 0
        self.moves = 0
        self.pairs_found = 0
        self.images = {}
        self.images_loaded = threading.Event()

        # Configura el tamaño del tablero según la dificultad
        if difficulty == "facil":
            self.board_size = (4, 4)
            self.cell_size = 100
        elif difficulty == "media":
            self.board_size = (6, 6)
            self.cell_size = 100
        elif difficulty == "dificil":
            self.board_size = (8, 8)
            self.cell_size = 75

            # Genera el tablero y carga las imágenes en segundo plano
        self._generate_board()
        self._load_images()

    def _generate_board(self):
        # Crea un conjunto de pares de identificadores de cartas y mezcla las posiciones
        total_pairs = (self.board_size[0] * self.board_size[1]) // 2
        cartas = list(range(1, total_pairs + 1)) * 2  # Pares duplicados de identificadores de imagen
        random.shuffle(cartas)

        # Divide en filas y columnas para formar el tablero
        self.tablero = [cartas[i:i + self.board_size[1]] for i in range(0, len(cartas), self.board_size[1])]

    def _load_images(self):
        # Carga las imágenes en un hilo separado
        def cargar():
            try:
                url_base = "https://dz3we2x72f7ol.cloudfront.net/expansions/151/en-us/SV3pt5_EN_"  # Cambiar por URL real de imágenes
                self.hidden_image = descargar_imagen(url_base + "206.png", (self.cell_size, self.cell_size))

                for i in range(1, (self.board_size[0] * self.board_size[1]) // 2 + 1):
                    self.images[i] = descargar_imagen(url_base + f"{i}.png", (self.cell_size, self.cell_size))

                # Indicar que las imágenes están cargadas
                self.images_loaded.set()
            except Exception as e:
                print(f"Error al cargar imágenes: {e}")

        hilo = threading.Thread(target=cargar)
        hilo.start()

    def images_are_loaded(self):
        # Verifica si todas las imágenes han sido cargadas
        return self.images_loaded.is_set()

    def start_timer(self):
        # Inicia o reinicia el temporizador de la partida
        self.start_time = time.time()

    def get_time(self):
        # Calcula el tiempo transcurrido en segundos
        return int(time.time() - self.start_time)

    def check_match(self, pos1, pos2):
        # Incrementa el contador de movimientos y verifica si las cartas coinciden
        self.moves += 1
        x1, y1 = pos1
        x2, y2 = pos2
        if self.tablero[x1][y1] == self.tablero[x2][y2]:
            self.pairs_found += 1
            return True
        return False

    def is_game_complete(self):
        # Verifica si el juego ha sido completado al encontrar todos los pares
        total_pairs = (self.board_size[0] * self.board_size[1]) // 2
        return self.pairs_found == total_pairs

    def save_score(self):
        # Guarda la puntuación del jugador en el archivo de puntuaciones
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nueva_puntuacion = {"nombre": self.player_name, "movimientos": self.moves, "fecha": fecha_actual}

        # Cargar puntuaciones actuales
        puntuaciones = self.load_scores()

        # Agregar la nueva puntuación y mantener solo las tres mejores por dificultad
        puntuaciones[self.difficulty].append(nueva_puntuacion)
        puntuaciones[self.difficulty] = sorted(puntuaciones[self.difficulty], key=lambda x: x["movimientos"])[:3]

        # Guardar el archivo actualizado
        with open("ranking.txt", "w") as archivo:
            for dificultad, scores in puntuaciones.items():
                for score in scores:
                    archivo.write(f"{dificultad},{score['nombre']},{score['movimientos']},{score['fecha']}\n")

    def load_scores(self):
        # Carga las puntuaciones desde el archivo, si existe
        puntuaciones = {"facil": [], "media": [], "dificil": []}

        try:
            with open("ranking.txt", "r") as archivo:
                for linea in archivo:
                    dificultad, nombre, movimientos, fecha = linea.strip().split(",")
                    puntuaciones[dificultad].append({"nombre": nombre, "movimientos": int(movimientos), "fecha": fecha})
        except FileNotFoundError:
            pass  # Si no existe el archivo, retorna puntuaciones vacías
        return puntuaciones

    def get_image_at(self, pos):
        """Devuelve el identificador de imagen en la posición dada."""
        row, col = pos
        image_id = self.tablero[row][col]
        return self.images[image_id]  # Retorna el objeto de imagen en lugar del id
