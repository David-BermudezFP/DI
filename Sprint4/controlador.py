import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel

from modelo import GameModel
from vista import MainMenu, GameView

class GameController:
    def __init__(self, root):
        # Inicializa la ventana principal, menú y otros atributos clave
        self.root = root
        self.model = None
        self.selected = []
        self.timer_started = False
        self.timer_running = False

        # Instancia el menú principal y define sus callbacks
        self.main_menu = MainMenu(
            root,
            start_game_callback=self.show_difficulty_selection,
            show_stats_callback=self.show_stats,
            quit_callback=self.root.quit
        )

    def show_difficulty_selection(self):
        # Pide la dificultad de juego al usuario
        difficulty = simpledialog.askstring("Seleccionar dificultad",
                                            "Selecciona la dificultad (facil, media, dificil):",
                                            parent=self.root).lower()  # Aseguramos que sea en minúsculas

        # Validamos que la dificultad sea correcta
        if difficulty not in ["facil", "media", "dificil"]:
            messagebox.showerror("Error", "Dificultad no válida. Debe ser 'facil', 'media' o 'dificil'.")
            return  # Si la dificultad no es válida, retornamos sin hacer nada más

        # Solicitar el nombre del jugador si la dificultad es válida
        player_name = self.main_menu.ask_player_name()
        if player_name:
            messagebox.showinfo("Nombre del Jugador", f"Bienvenido {player_name}, ¡Buena suerte!")
        else:
            messagebox.showwarning("Nombre del Jugador", "No se proporcionó un nombre. Continuando sin nombre.")

        # Aquí, después de seleccionar la dificultad y el nombre, el juego puede empezar.
        self.start_game(difficulty, player_name)

    def start_game(self, difficulty, player_name):
        # Inicia una nueva partida con la dificultad seleccionada
        self.show_loading_window("Cargando juego...")
        self.model = GameModel(difficulty, player_name)
        self.check_images_loaded()

    def show_loading_window(self, message):
        # Crea una ventana de carga temporal
        self.loading_window = Toplevel(self.root)
        self.loading_window.title("Cargando")
        label = tk.Label(self.loading_window, text=message)
        label.pack(padx=20, pady=20)
        self.loading_window.grab_set()

    def check_images_loaded(self):
        # Comprueba si las imágenes están cargadas y si es así, inicializa GameView
        if self.model.images_are_loaded():
            self.loading_window.destroy()
            self.game_view = GameView(
                on_card_click_callback=self.on_card_click,
                update_move_count_callback=self.update_move_count,
                update_time_callback=self.update_time
            )
            self.game_view.create_board(self.model)
            self.timer_running = True
            self.update_time()
        else:
            # Vuelve a comprobar tras un pequeño retraso
            self.root.after(100, self.check_images_loaded)

    def on_card_click(self, pos):
        """Maneja el evento de clic en una carta."""
        # Iniciar el temporizador si es la primera vez que se hace clic en una carta
        if not self.timer_started:
            self.model.start_timer()
            self.timer_started = True

        # Verificar si la carta no está ya seleccionada
        if pos not in self.selected:
            # Agregar la posición a la lista de seleccionadas
            self.selected.append(pos)

            # Obtener el objeto de imagen para la carta en la posición seleccionada
            image_obj = self.model.get_image_at(pos)

            # Actualizar la vista de la carta con la imagen
            self.game_view.update_board(pos, image_obj)

            # Si se han seleccionado dos cartas, manejar la selección
            if len(self.selected) == 2:
                self.handle_card_selection()

    def handle_card_selection(self):
        # Verifica si las dos cartas seleccionadas coinciden
        pos1, pos2 = self.selected
        is_match = self.model.check_match(pos1, pos2)
        self.update_move_count(self.model.moves)

        if is_match:
            self.selected.clear()
            if self.check_game_complete():
                messagebox.showinfo("¡Victoria!", "¡Has completado el juego!")
                self.return_to_main_menu()
        else:
            # Si no coinciden, ocultar las cartas después de un pequeño retraso
            self.root.after(1000, lambda: self.reset_selected_cards(pos1, pos2))

    def reset_selected_cards(self, pos1, pos2):
        # Pasa la imagen oculta al método reset_cards en GameView
        hidden_image = self.model.hidden_image
        self.game_view.reset_cards(pos1, pos2, hidden_image)
        self.selected.clear()

    def update_move_count(self, moves):
        # Actualiza el contador de movimientos en la interfaz
        self.game_view.update_move_count(moves)

    def check_game_complete(self):
        # Verifica si el jugador ha completado el juego
        if self.model.is_game_complete():
            self.model.save_score()
            return True
        return False

    def return_to_main_menu(self):
        # Cierra el tablero de juego y regresa al menú principal
        self.game_view.destroy()
        self.main_menu.root.deiconify()

    def show_stats(self):
        # Muestra las estadísticas de los mejores puntajes
        stats = self.model.load_scores()
        self.main_menu.show_stats(stats)

    def update_time(self):
        # Actualiza el temporizador en la vista del juego
        if self.timer_running:
            elapsed_time = self.model.get_time()
            self.game_view.update_time(elapsed_time)
            self.root.after(1000, self.update_time)
