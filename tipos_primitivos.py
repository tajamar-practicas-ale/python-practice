# Entero (int)
entero = 21
print("Tipo entero: (int)")
print(f"Valor: {entero}")
print(f"Dominio: Números enteros (negativos, cero y positivos)")
print(f"Operadores: +, -, *, /, //, %")
print(f"Tipo identificativo: {type(entero)}\n")

# Reales (float)
real = 6.9
print("Tipo real: (float)")
print(f"Valor:  {real}")
print(f"Dominio: Números decimales (números de punto flotante)")
print(f"Operadores: +, -, *, /, **")
print(f"Tipo identificativo: {type(real)}\n")

# Caracteres (str)
caracter = "la cebolla"
print("Tipo caracter: (str)")
print(f"Valor: {caracter}")
print(f"Dominio: cualquier caracter o cadena de texto")
print(f"Operadores: + (concatenación), ** (repetición), y += (adición)")
print(f"Tipo identificativo: {type(caracter)}\n")

# Arrays/lista ([])
array = [1,5.2,3,"array"]
print("Tipo caracter: ('{}')")
print(f"Valor: {array}")
print(f"Dominio: secuencias de elementos (pueden ser mixtos)")
print(f"Operadores: + (concatenación), ** (repetición), len(), append()")
print(f"Tipo identificativo: {type(array)}\n")

# Tupla (())
tupla = (1,5.2,3,"tupla")
print("Tipo caracter: ('[]')")
print(f"Valor: {tupla}")
print(f"Dominio: secuencias de elementos (pueden ser mixtos y no se pueden modificar)")
print(f"Operadores: + (concatenación), ** (repetición)")
print(f"Tipo identificativo: {type(tupla)}\n")

# Diccionarios ({"x":y})
dict = {"numero": 1, "operador": "suma"}
print("Tipo caracter: ('{'x':y}')")
print(f"Valor: {dict}")
print(f"Dominio: colecciones de par clave-valor")
print("Operadores: {}, .get(), .keys(), .values()")
print(f"Tipo identificativo: {type(dict)}\n")

# Diccionarios ({"x":y})
from enum import Enum
    
class Colores(Enum):
    ROJO = 1
    VERDE = 2
    AZUL = 3

print("Tipo de caracter: (Enum)")
color = Colores.ROJO
print(f"Valor: {color.name} = {color.value}")
print(f"Dominio: Conjunto de valores constantes")
print(f"Operadores: .name, .value")
print(f"Tipo identificativo: {type(color)}\n")