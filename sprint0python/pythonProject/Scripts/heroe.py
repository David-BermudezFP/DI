class Heroe:

    # Constructor que inicializa el héroe con su nombre y atributos básicos de combate
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del héroe
        self.ataque = 10  # Puntos de ataque del héroe
        self.defensa = 10  # Puntos de defensa del héroe
        self.salud = 50  # Salud inicial del héroe
        self.salud_maxima = 50  # Salud máxima que puede alcanzar el héroe
        self.defensa_maxima = self.defensa  # Valor original de defensa, para reestablecerlo luego de usar defensa

    # Método para que el héroe ataque a un enemigo
    def atacar(self, enemigo):
        print(f"Héroe ataca a {enemigo.nombre}")
        danho_enemigo = self.ataque - enemigo.defensa  # Calcula el daño después de la defensa del enemigo
        if danho_enemigo > 0:  # Solo se aplica daño si es mayor que la defensa del enemigo
            enemigo.salud -= danho_enemigo  # Reduce la salud del enemigo según el daño calculado
            print(f"El enemigo {enemigo.nombre} ha recibido {danho_enemigo} puntos de daño")
            print(f"Salud restante del enemigo: {enemigo.salud}")
            if enemigo.salud <= 0:  # Verifica si el enemigo ha muerto
                print(f"El enemigo {enemigo.nombre} ha muerto")
        else:
            # Si el daño es menor o igual a la defensa, el ataque es bloqueado
            print("El enemigo ha bloqueado el ataque.")

    # Método para que el héroe se cure
    def curarse(self):
        curacion = 15  # Puntos de curación
        # Se asegura que la curación no exceda la salud máxima del héroe
        curacion_real = min(self.salud_maxima - self.salud, curacion)
        self.salud += curacion  # Aumenta la salud del héroe
        if self.salud > self.salud_maxima:  # Ajusta la salud si excede el máximo
            self.salud = self.salud_maxima
        print(f"Héroe se ha curado {curacion_real} puntos de salud. Salud actual: {self.salud}")

    # Método para que el héroe se defienda aumentando temporalmente su defensa
    def defenderse(self):
        self.defensa += 50  # Aumenta la defensa temporalmente
        print(f"Héroe se defiende. Defensa aumentada temporalmente a {self.defensa}")

    # Método para restablecer la defensa a su valor original
    def reset_defensa(self):
        self.defensa = self.defensa_maxima  # Reinicia la defensa al valor inicial
        print(f"La defensa de {self.nombre} vuelve a la normalidad")

    # Método para verificar si el héroe está vivo
    def esta_vivo(self):
        if self.salud > 0:  # El héroe está vivo si su salud es mayor a 0
            return True
        else:
            return False