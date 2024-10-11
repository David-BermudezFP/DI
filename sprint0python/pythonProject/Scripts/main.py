from Scripts.heroe import Heroe
from Scripts.mazmorra import Mazmorra

# Función principal del programa que inicia la aventura
def main():
    # Solicita al usuario que introduzca el nombre de su héroe
    nombre_heroe = input("Introduce el nombre de tu héroe: ")
    # Crea una instancia de la clase Heroe usando el nombre ingresado
    heroe = Heroe(nombre_heroe)

    # Crea una instancia de la clase Mazmorra y le pasa al héroe
    mazmorra = Mazmorra(heroe)
    # Inicia el juego en la mazmorra
    mazmorra.jugar()

# Comprueba si el script se está ejecutando directamente
if __name__ == "__main__":
    main()
