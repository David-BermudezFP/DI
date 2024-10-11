#Realización de forma procedural

from operaciones import suma, resta, multiplicacion, division

# Función para solicitar dos números al usuario
def solicitar_numeros():
    # Solicita el primer número y lo convierte a tipo float
    a = float(input("Ingresa el primer número: "))
    # Solicita el segundo número y lo convierte a tipo float
    b = float(input("Ingresa el segundo número: "))
    return a, b  # Retorna ambos números

# Función principal del programa
def main():
    while True:
        # Solicita dos números al usuario
        a, b = solicitar_numeros()

        # Solicita la operación deseada
        print("Operaciones disponibles: suma, resta, multiplicacion, division")
        operacion = input("¿Qué operación deseas realizar? (suma/resta/multiplicacion/division): ").lower()

        # Realiza la operación seleccionada
        if operacion == "suma":
            resultado = suma(a, b)  # Llama a la función suma
        elif operacion == "resta":
            resultado = resta(a, b)  # Llama a la función resta
        elif operacion == "multiplicacion":
            resultado = multiplicacion(a, b)  # Llama a la función multiplicacion
        elif operacion == "division":
            resultado = division(a, b)  # Llama a la función division
        else:
            print("Operación no válida.")  # Mensaje de error si la operación no es válida
            continue

        # Muestra el resultado de la operación
        print(f"El resultado de la {operacion} es: {resultado}")

        # Pregunta al usuario si desea realizar otra operación
        continuar = input("¿Quieres hacer otra operación? (s/n): ").lower()
        if continuar != "s":  # Si la respuesta no es 's', se termina el ciclo
            print("¡Gracias por usar la calculadora!")
            break

# Comprueba si el archivo se está ejecutando directamente
if __name__ == "__main__":
    main()


# Realizacion de forma orientada a objetos
#
# from operaciones import Operaciones
#
# class Calculadora:
#
#     def __init__(self):
#         # Crear una instancia de la clase Operaciones
#         self.operaciones = Operaciones()
#
#     def solicitar_numeros(self):
#         """Función para solicitar dos números al usuario."""
#         a = float(input("Ingresa el primer número: "))
#         b = float(input("Ingresa el segundo número: "))
#         return a, b
#
#     def realizar_operacion(self):
#         """Función que solicita operación y la ejecuta."""
#         a, b = self.solicitar_numeros()
#
#         # Solicitar la operación
#         print("Operaciones disponibles: suma, resta, multiplicacion, division")
#         operacion = input("¿Qué operación deseas realizar? (suma/resta/multiplicacion/division): ").lower()
#
#         # Ejecutar la operación seleccionada
#         if operacion == "suma":
#             resultado = self.operaciones.suma(a, b)
#         elif operacion == "resta":
#             resultado = self.operaciones.resta(a, b)
#         elif operacion == "multiplicacion":
#             resultado = self.operaciones.multiplicacion(a, b)
#         elif operacion == "division":
#             resultado = self.operaciones.division(a, b)
#         else:
#             print("Operación no válida.")
#             return None
#
#         print(f"El resultado de la {operacion} es: {resultado}")
#
#     def ejecutar(self):
#         """Función principal de la calculadora que permite realizar varias operaciones."""
#         while True:
#             self.realizar_operacion()
#
#             # Preguntar si el usuario desea continuar
#             continuar = input("¿Quieres hacer otra operación? (s/n): ").lower()
#             if continuar != "s":
#                 print("¡Gracias por usar la calculadora!")
#                 break