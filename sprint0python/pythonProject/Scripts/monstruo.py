class Monstruo:

    # Constructor que inicializa el monstruo con su nombre y atributos de combate
    def __init__(self, nombre, ataque, defensa, salud):
        self.nombre = nombre  # Nombre del monstruo
        self.ataque = ataque  # Puntos de ataque del monstruo
        self.defensa = defensa  # Puntos de defensa del monstruo
        self.salud = salud  # Salud inicial del monstruo

    # Método para que el monstruo ataque a un héroe
    def atacar(self, heroe):
        print(f"El monstruo {self.nombre} ataca a {heroe.nombre}.")
        danho = self.ataque - heroe.defensa  # Calcula el daño después de la defensa del héroe
        if danho > 0:  # Solo se aplica daño si es mayor que la defensa del héroe
            heroe.salud -= danho  # Reduce la salud del héroe según el daño calculado
            print(f"El héroe ha recibido {danho} puntos de daño.")
            print(f"Vida restante del héroe: {heroe.salud}")
        else:
            # Si el daño es menor o igual a la defensa, el ataque es bloqueado
            print(f"El héroe ha bloqueado el ataque.")

    # Método para verificar si el monstruo está vivo
    def esta_vivo(self):
        if self.salud > 0:  # El monstruo está vivo si su salud es mayor a 0
            return True
        else:
            return False