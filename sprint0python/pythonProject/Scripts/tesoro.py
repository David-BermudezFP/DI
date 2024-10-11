import random

class Tesoro:

    # Constructor que inicializa el tesoro con una lista de beneficios posibles
    def __init__(self):
        # Beneficios disponibles al encontrar un tesoro
        self.beneficios = ["aumento de ataque", "aumento de defensa", "restauración de salud"]

    # Método para aplicar un beneficio aleatorio al héroe cuando encuentra un tesoro
    def encontrar_tesoro(self, heroe):
        tesoro_encontrado = random.choice(self.beneficios)  # Selecciona un beneficio aleatorio
        print(f"Héroe ha encontrado un tesoro: {tesoro_encontrado}")

        # Verifica el tipo de tesoro encontrado y aplica el beneficio correspondiente al héroe
        if tesoro_encontrado == "aumento de ataque":
            # Incrementa el ataque del héroe en un valor aleatorio entre 1 y 5
            heroe.ataque += random.randint(1, 5)
            print(f"El ataque de {heroe.nombre} aumenta a {heroe.ataque}")
        elif tesoro_encontrado == "aumento de defensa":
            # Incrementa la defensa del héroe en un valor aleatorio entre 1 y 5
            heroe.defensa += random.randint(1, 5)
            # Actualiza también la defensa máxima del héroe al nuevo valor de defensa
            heroe.defensa_maxima = heroe.defensa
            print(f"La defensa de {heroe.nombre} aumenta a {heroe.defensa}")
        elif tesoro_encontrado == "restauración de salud":
            # Restaura la salud del héroe en un valor aleatorio entre 10 y 30
            heroe.salud += random.randint(10, 30)
            # Verifica que la salud del héroe no exceda su salud máxima
            if heroe.salud > heroe.salud_maxima:
                heroe.salud = heroe.salud_maxima
            print(f"La salud de {heroe.nombre} ha sido restaurada a {heroe.salud}")
