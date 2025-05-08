n1 = 15
n2 = 20

mensaje1 = "hola"

# Las funciones siempre retornan algo

# función sin parámetros
def funcion1(): 
    resultado = n1 + n2
    print(f"la suma de 15 + 20 es {resultado}\n")
    return resultado
funcion1()

# función con parámetros
num = int(input("¿Qué número quieres multiplicar por 2?: "))

def funcion2(num):
    resultado = num * 2
    print(f"{num} multiplicado por 2 es {resultado}\n")
    return resultado
funcion2(num)

# Los procedimientos son acciones que no retornan algo

# procedimiento sin parámetros
def proc1():
    global mensaje1
    mensaje1="mensaje cambiado"
    print(f"el mensaje 'hola' fue cambiado por {mensaje1}\n")
proc1()

# procedimiento con parámetros
mensaje = str(input("¿Qué mensaje quieres imprimir?: "))

def proc2(mensaje):
    print(mensaje)
proc2(mensaje)
