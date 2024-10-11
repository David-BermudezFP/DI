#Realización de forma procedural

# Función para sumar dos números
def suma(a, b):
    return a + b  # Retorna la suma de 'a' y 'b'

# Función para restar dos números
def resta(a, b):
    return a - b  # Retorna la resta de 'b' de 'a'

# Función para multiplicar dos números
def multiplicacion(a, b):
    return a * b  # Retorna el producto de 'a' y 'b'

# Función para dividir dos números
def division(a, b):
    # Verifica que 'b' no sea cero para evitar división por cero
    if b == 0:
        return "Error: División por cero no es permitida"
    return a / b  # Retorna el resultado de 'a' dividido por 'b'


# Realizacion de forma orientada a objetos
#
# class Operaciones:
#
#     def suma(self, a, b):
#         return a + b
#
#     def resta(self, a, b):
#         return a - b
#
#     def multiplicacion(self, a, b):
#         return a * b
#
#     def division(self, a, b):
#         if b == 0:
#             return "Error: División por cero no es permitida"
#         return a / b
