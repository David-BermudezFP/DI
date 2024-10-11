from Scripts.monstruo import Monstruo
from Scripts.tesoro import Tesoro

class Mazmorra:

    # Constructor que inicializa la mazmorra con un héroe, una lista de monstruos y un objeto de tesoro
    def __init__(self, heroe):
        self.heroe = heroe  # El héroe que explorará la mazmorra
        self.monstruo = [  # Lista de monstruos que el héroe enfrentará
            Monstruo(nombre="Yordle", ataque=12, defensa=5, salud=30),
            Monstruo(nombre="Vastaya", ataque=15, defensa=4, salud=25),
            Monstruo(nombre="Darkin", ataque=20, defensa=7, salud=40)
        ]
        self.tesoro = Tesoro()  # Objeto tesoro que el héroe puede encontrar al derrotar monstruos

    # Método principal para comenzar la aventura en la mazmorra
    def jugar(self):
        print("Héroe entra en la mazmorra")
        # Ciclo del juego: el héroe lucha con monstruos hasta que los derrote a todos o muera
        while self.monstruo and self.heroe.esta_vivo():
            enemigo = self.monstruo.pop(0)  # El héroe enfrenta al primer monstruo de la lista
            print(f"Te has encontrado con un {enemigo.nombre}.")
            self.enfrentar_enemigo(enemigo)  # Inicia el combate contra el monstruo

        # Mensaje final según el resultado
        if self.heroe.esta_vivo():
            print(f"¡{self.heroe.nombre} ha derrotado a todos los monstruos y ha conquistado la mazmorra!")
        else:
            print("Héroe ha sido derrotado en la mazmorra.")

    # Método para gestionar el combate entre el héroe y un monstruo
    def enfrentar_enemigo(self, enemigo):
        # El combate continúa mientras tanto el héroe como el monstruo sigan vivos
        while enemigo.esta_vivo() and self.heroe.esta_vivo():
            opcion_valida = False  # Bandera para asegurar que la opción seleccionada es válida
            while not opcion_valida:
                print("¿Qué deseas hacer?")
                print("1. Atacar")
                print("2. Defender")
                print("3. Curarse")

                opcion = input("Selecciona una opción: ")
                if opcion == "1":
                    self.heroe.atacar(enemigo)  # El héroe ataca al monstruo
                    opcion_valida = True
                elif opcion == "2":
                    self.heroe.defenderse()  # El héroe incrementa su defensa
                    opcion_valida = True
                elif opcion == "3":
                    self.heroe.curarse()  # El héroe recupera salud
                    opcion_valida = True
                else:
                    print("Opción no válida.")  # Mensaje de error si la opción es incorrecta

            # Si el monstruo sigue vivo, contraataca al héroe
            if enemigo.esta_vivo():
                enemigo.atacar(self.heroe)  # El monstruo ataca al héroe
                self.heroe.reset_defensa()  # La defensa del héroe se restablece al valor original

        # Después de la batalla, si el héroe ha derrotado al monstruo, se busca un tesoro
        if not enemigo.esta_vivo():
            self.heroe.reset_defensa()  # La defensa del héroe se restablece después del combate
            self.buscar_tesoro()  # Oportunidad de encontrar un tesoro

    # Método para buscar tesoro después de derrotar a un monstruo
    def buscar_tesoro(self):
        print("Buscando tesoro...")
        self.tesoro.encontrar_tesoro(self.heroe)  # El héroe obtiene un beneficio aleatorio
