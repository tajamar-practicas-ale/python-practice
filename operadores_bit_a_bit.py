# Los operadores bit a bit realizan operaciones directamente sobre los números enteros

"""
Binario base 2 por ejemplo:

5 = 101
3 = 011

"""

# 1. AND (&) Compara cada bit de los números y devuelve 1 solo si ambos bits son 1
# de lo contrario, devuelve 0

a = 5   # 0101 en binario
b = 3   # 0011 en binario

resultado = a & b  # AND bit a bit
print(resultado)  # Salida: 1 (que es 0001 en binario)

# 2. OR (|) Compara cada bit de los números y devuelve 1 si al menos uno de ellos es 1,
# de lo contrario, devuelve 0

a = 5   # 0101 en binario
b = 3   # 0011 en binario

resultado = a | b  # OR bit a bit
print(resultado)  # Salida: 7 (que es 0111 en binario)

# 3. XOR (^) Compara cada bit de los números y devuelve 1 si los bits son diferentes,
# de lo contrario, devuelve 0

a = 5   # 0101 en binario
b = 3   # 0011 en binario

resultado = a ^ b  # XOR bit a bit
print(resultado)  # Salida: 6 (que es 0110 en binario)

# 4. NOT (~) bit a bit invierte todos los bits de un número (Cambia 1 a 0 y 0 a 1). Solo es aplicable a un número

a = 5   # 0101 en binario

resultado = ~a  # NOT bit a bit
print(resultado)  # Salida: -6 (en binario, se obtiene el complemento a 2)

# 5. Desplazamiento a la izquierda (<<)
# Mueve los bits de un número a la izquierda, agregando 0 en los lugares vacíos
# Es equivalente a multiplicar el número 2 por cada posición de desplazamiento

a = 5   # 0101 en binario

resultado = a << 1  # Desplazar a la izquierda 1 vez
print(resultado)  # Salida: 10 (que es 1010 en binario)

# 6. Desplazamiento a la derecha (>>)
# Mueve los bits de un número a la derecha, eliminando los bits más a la derecha
# Es equivalente a dividir el número por 2 por cada posición de desplazamiento

a = 5   # 0101 en binario

resultado = a >> 1  # Desplazar a la derecha 1 vez
print(resultado)  # Salida: 2 (que es 0010 en binario)


