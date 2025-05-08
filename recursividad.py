# Una función recursiva es una función que se llama a sí misma
def factorial(n):
    if n == 0 or n == 1:      # Caso base
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva

# Uso
print(factorial(5))  # Salida: 120
