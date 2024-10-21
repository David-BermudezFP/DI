import tkinter as tk
import random
from mailbox import mboxMessage
from statistics import multimode
from tkinter import mainloop, messagebox, IntVar
from tkinter.constants import DISABLED, NORMAL

from select import select

# Crea la ventana principal de la aplicación
root = tk.Tk()
root.title("Ejercicio Extra")
root.geometry("300x200")


def jugarsolo():
    solo = tk.Toplevel(root)
    solo.title("Singleplayer")
    solo.geometry("500x300")

    def jugar(jugada_usuario):
        jugada_maquina = random.choice(["piedra", "papel", "tijera"])
        if jugada_usuario == jugada_maquina:
            resultado = "Empate"
        elif ((jugada_usuario == "piedra" and jugada_maquina == "tijera") or
              (jugada_usuario == "papel" and jugada_maquina == "piedra") or
              (jugada_usuario == "tijera" and jugada_maquina == "papel")):
            resultado = "Ganaste"
        else:
            resultado = "Perdiste"
        jugadalabel.configure(text=f"Jugada Usuario: {jugada_usuario} \t Jugada Maquina: {jugada_maquina}"
                                   f"\n Resultado: {resultado}")


    # Añadimos botones para piedra, papel y tijeras
    piedrab = tk.Button(solo, text="Piedra", command=lambda: jugar("piedra"))
    piedrab.pack(pady=10, padx=10)
    papelb = tk.Button(solo, text="Papel", command=lambda: jugar("papel"))
    papelb.pack(pady=10, padx=10)
    tijerab = tk.Button(solo, text="Tijera", command=lambda: jugar("tijera"))
    tijerab.pack(pady=10, padx=10)
    jugadalabel = tk.Label(solo, text="")
    jugadalabel.pack(pady=10, padx=10)
    salirsolo = tk.Button(solo, text="Salir", command =lambda: solo.destroy())
    salirsolo.pack(pady=10, padx=10)

def multiplayer():
    # Variables para almacenar las selecciones de cada jugador
    global contador
    contador = tk.IntVar()
    contador.set(0)
    victorias1 = tk.IntVar()
    victorias1.set(0)
    victorias2 = tk.IntVar()
    victorias2.set(0)


    # Interfaz gráfica
    partidamultiplayer = tk.Toplevel(root)
    partidamultiplayer.title("Multiplayer")
    partidamultiplayer.geometry("300x300")
    label1 = tk.Label(partidamultiplayer, text="Jugador 1: Elige tu jugada", font=("Arial", 14))
    label1.pack(pady=10)

    frame_jugador1 = tk.Frame(partidamultiplayer)
    frame_jugador1.pack(pady=10)

    boton_piedra_j1 = tk.Button(frame_jugador1, text="Piedra", command=lambda: seleccion_j1("Piedra"), width=10)
    boton_piedra_j1.grid(row=0, column=0)

    boton_papel_j1 = tk.Button(frame_jugador1, text="Papel", command=lambda: seleccion_j1("Papel"), width=10)
    boton_papel_j1.grid(row=0, column=1)

    boton_tijeras_j1 = tk.Button(frame_jugador1, text="Tijeras", command=lambda: seleccion_j1("Tijeras"), width=10)
    boton_tijeras_j1.grid(row=0, column=2)

    label2 = tk.Label(partidamultiplayer, text="Jugador 2: Elige tu jugada", font=("Arial", 14))
    label2.pack(pady=10)

    frame_jugador2 = tk.Frame(partidamultiplayer)
    frame_jugador2.pack(pady=10)

    boton_piedra_j2 = tk.Button(frame_jugador2, text="Piedra", command=lambda: seleccion_j2("Piedra"), width=10)
    boton_piedra_j2.grid(row=2, column=0)

    boton_papel_j2 = tk.Button(frame_jugador2, text="Papel", command=lambda: seleccion_j2("Papel"), width=10)
    boton_papel_j2.grid(row=2, column=1)

    boton_tijeras_j2 = tk.Button(frame_jugador2, text="Tijeras", command=lambda: seleccion_j2("Tijeras"), width=10)
    boton_tijeras_j2.grid(row=2, column=2)

    # Función para seleccionar la jugada del jugador 1
    def seleccion_j1(eleccion):
        global seleccion_jugador1
        contador.set(value=contador.get()+1)
        boton_papel_j1.configure(state=DISABLED)
        boton_tijeras_j1.configure(state=DISABLED)
        boton_piedra_j1.configure(state=DISABLED)
        seleccion_jugador1 = eleccion
        if contador.get()== 2:
            verificar_selecciones()

    # Función para seleccionar la jugada del jugador 2
    def seleccion_j2(eleccion):
        global seleccion_jugador2
        contador.set(value=contador.get()+1)
        boton_papel_j2.configure(state=DISABLED)
        boton_tijeras_j2.configure(state=DISABLED)
        boton_piedra_j2.configure(state=DISABLED)
        seleccion_jugador2 = eleccion
        if contador.get()== 2:
            verificar_selecciones()


    # Verificar si ambos jugadores han hecho su selección
    def verificar_selecciones():
        if seleccion_jugador1 and seleccion_jugador2:
            determinar_ganador()

    # Se compara el valor de las selecciones y se selecciona ganador, perdedor o empate
    # Función para determinar el ganador
    def determinar_ganador():
        global seleccion_jugador1, seleccion_jugador2

        if seleccion_jugador1 == seleccion_jugador2:
            resultado = "Empate"
        elif (seleccion_jugador1 == "Piedra" and seleccion_jugador2 == "Tijeras") or \
                (seleccion_jugador1 == "Tijeras" and seleccion_jugador2 == "Papel") or \
                (seleccion_jugador1 == "Papel" and seleccion_jugador2 == "Piedra"):
            resultado = "Jugador 1 ha ganado"
            victorias1.set(value=victorias1.get()+1)
        else:
            resultado = "Jugador 2 ha ganado"
            victorias2.set(value=victorias2.get()+1)

        # Mostrar el resultado en un MessageBox
        messagebox.showinfo("Resultado", resultado)

        # Reiniciar selecciones
        seleccion_jugador1 = None
        seleccion_jugador2 = None
        contador.set(value=0)
        boton_papel_j1.configure(state=NORMAL)
        boton_tijeras_j1.configure(state=NORMAL)
        boton_piedra_j1.configure(state=NORMAL)
        boton_papel_j2.configure(state=NORMAL)
        boton_tijeras_j2.configure(state=NORMAL)
        boton_piedra_j2.configure(state=NORMAL)

        if victorias1.get() == 3:
            messagebox.showinfo("Resultado", f"El ganador es el Jugador 1 \n \t {victorias1.get()} - {victorias2.get()} ")
            partidamultiplayer.destroy()

        elif victorias2.get() == 3:
            messagebox.showinfo("Resultado", f"El ganador es el Jugador 2 \n \t {victorias2.get()} - {victorias1.get()} ")
            partidamultiplayer.destroy()





botonsolo = tk.Button(root,text="Singleplayer", command=jugarsolo)
botonsolo.pack(pady=10, padx=10)
botonmulti = tk.Button(root,text="Multiplayer", command=multiplayer)
botonmulti.pack(pady=10, padx=10)
botonsalir = tk.Button(root,text="Salir", command=root.quit)
botonsalir.pack(pady=10, padx=10)

# Inicia el bucle principal de la interfaz gráfica
root.mainloop()