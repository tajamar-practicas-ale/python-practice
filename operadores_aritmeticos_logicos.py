n1 = 60
n2 = 2

a = True
b = False

# Operadores aritméticos
suma = n1 + n2
resta = n1 - n2
mult = n1 * n2
div = n1 / n2
div_ent = n1 // n2 # División entera
mod = n1 % n2 # Módulo o residuo de la división
exp = n1 ** n2 # exponenciación 

print("OPERADORES ARITMÉTICOS")
print(" ")
print(f"{n1} + {n2} = {suma}")
print(f"{n1} - {n2} = {resta}")
print(f"{n1} * {n2} = {mult}")
print(f"{n1} / {n2} = {div}")
print(f"{n1} // {n2} = {div_ent}")
print(f"{n1} % {n2} = {mod}")
print(f"{n1} ** {n2} = {exp}")
print("\n")

print("OPERADORES LÓGICOS")
print(" ")
print(f"a and b = {a and b}") # Retorna True si ambos son True
print(f"a and b = {a or b}") # Retorna True si uno de ellos es True
print(f"a and b = {not a}") # Invierte el valor