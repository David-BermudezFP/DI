import tkinter as tk
from tkinter import simpledialog, Toplevel


class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback, update_time_callback):
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback
        self.labels = []
        self.root = None
        self.move_count_label = None
        self.time_label = None

    def create_board(self, model):
        # Crea una ventana de juego como Toplevel
        self.root = Toplevel()
        self.root.title("Juego de Memoria")

        # Define la cuadrícula del tablero usando el modelo
        rows, cols = model.board_size
        for r in range(rows):
            row_labels = []
            for c in range(cols):
                # Crear una etiqueta para cada carta y asignar la imagen oculta
                label = tk.Label(self.root, image=model.hidden_image)
                label.grid(row=r, column=c, padx=5, pady=5)
                label.bind("<Button-1>", lambda e, pos=(r, c): self.on_card_click_callback(pos))
                row_labels.append(label)
            self.labels.append(row_labels)

        # Agrega el contador de movimientos
        self.move_count_label = tk.Label(self.root, text="Movimientos: 0")
        self.move_count_label.grid(row=rows, column=0, columnspan=cols // 2, sticky="w")

        # Agrega el temporizador
        self.time_label = tk.Label(self.root, text="Tiempo: 0 s")
        self.time_label.grid(row=rows, column=cols // 2, columnspan=cols // 2, sticky="e")

    def update_board(self, pos, image_id):
        # Actualiza la imagen de la carta en la posición especificada
        r, c = pos
        self.labels[r][c].configure(image=image_id)
        self.labels[r][c].image = image_id

    def reset_cards(self, pos1, pos2, hidden_image):
        # Restaura las imágenes de las cartas a su imagen oculta
        r1, c1 = pos1
        r2, c2 = pos2
        self.labels[r1][c1].configure(image=hidden_image)
        self.labels[r2][c2].configure(image=hidden_image)

    def update_move_count(self, moves):
        # Actualiza el texto del contador de movimientos
        self.move_count_label.config(text=f"Movimientos: {moves}")

    def update_time(self, time):
        # Actualiza el temporizador en la interfaz
        self.time_label.config(text=f"Tiempo: {time} s")

    def destroy(self):
        # Cierra la ventana del juego y limpia los elementos de la vista
        if self.root:
            self.root.destroy()
            self.labels.clear()


class MainMenu:
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        # Crear la ventana principal del menú
        self.root = root
        self.root.title("Menú Principal")

        # Crear los botones
        self.start_game_button = tk.Button(self.root, text="Jugar", command=start_game_callback)
        self.start_game_button.pack(pady=10)

        self.show_stats_button = tk.Button(self.root, text="Estadísticas", command=show_stats_callback)
        self.show_stats_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Salir", command=quit_callback)
        self.quit_button.pack(pady=10)

    def ask_player_name(self):
        """Abre un cuadro de diálogo para preguntar el nombre del jugador"""
        player_name = simpledialog.askstring("Nombre del Jugador", "Por favor, ingresa tu nombre:")
        return player_name

    def show_stats(self, stats):
        # stats: diccionario con las puntuaciones por dificultad
        ventana_stats = Toplevel(self.root)
        ventana_stats.title("Estadísticas")

        for dificultad, puntuaciones in stats.items():
            tk.Label(ventana_stats, text=f"Dificultad: {dificultad}").pack()

            if puntuaciones:
                for score in puntuaciones:
                    tk.Label(
                        ventana_stats,
                        text=f"{score['nombre']} - {score['movimientos']} movimientos - {score['fecha']}"
                    ).pack()
            else:
                tk.Label(ventana_stats, text="Sin registros").pack()
