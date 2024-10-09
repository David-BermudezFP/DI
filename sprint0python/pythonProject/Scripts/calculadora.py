#PROCEDURAL

from operaciones import suma, resta, multiplicacion, division
def solicitar_numeros():
    # Función para solicitar dos números al usuario
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    return a, b

def main():
    while True:
        # Solicitar los números al usuario
        a, b = solicitar_numeros()

        # Solicitar la operación
        print("Operaciones disponibles: suma, resta, multiplicacion, division")
        operacion = input("¿Qué operación deseas realizar? (suma/resta/multiplicacion/division): ").lower()

        # Ejecutar la operación seleccionada
        if operacion == "suma":
            resultado = suma(a, b)
        elif operacion == "resta":
            resultado = resta(a, b)
        elif operacion == "multiplicacion":
            resultado = multiplicacion(a, b)
        elif operacion == "division":
            resultado = division(a, b)
        else:
            print("Operación no válida.")
            continue

        # Mostrar el resultado
        print(f"El resultado de la {operacion} es: {resultado}")

        # Preguntar si quiere hacer otra operación
        continuar = input("¿Quieres hacer otra operación? (s/n): ").lower()
        if continuar != "s":
            print("¡Gracias por usar la calculadora!")
            break

# Verificar si este archivo se está ejecutando directamente
if __name__ == "__main__":
    main()


#ORIENTADO A OBJETOS

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