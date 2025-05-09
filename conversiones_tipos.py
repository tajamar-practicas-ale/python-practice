# Ejemplo de conversión implícita 
# (Python convierte automáticamente tipos de datos)
a = 10      # entero
b = 3.5     # float
c = a + b   # Python convierte 'a' en float automáticamente

print(c)        # 13.5
print(type(c))  # <class 'float'>

# Ejemplos de conversión explícita
# (Se fuerza la conversión de un tipo a otro)

# De float a int
numero = 5.987
entero = int(numero)
print(entero)  # 5

# De int a float
entero = 42
decimal = float(entero)
print(decimal)  # 42.0

# De int a str
edad = 30
texto = str(edad)
print("Tu edad es " + texto)  # Tu edad es 30

# De str a número (solo si el str es numérico)
cadena = "123"
numero = int(cadena)
print(numero + 10)  # 133

# De str decimal a float
cadena = "3.1416"
pi = float(cadena)
print(pi + 1)  # 4.1416

# De cualquier tipo de dato a booleano (0, cadena vacía o None son False)
print(bool(0))    # False
print(bool(42))   # True
print(bool(-3.5)) # True
print(bool("")) # False

# De lista a conjunto (elimina duplicados)
lista = [1, 2, 2, 3]
conjunto = set(lista)
print(conjunto)  # {1, 2, 3}