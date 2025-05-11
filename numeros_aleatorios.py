import random

# Simular el lanzamiento de un dado
def lanzar_dado():
    resultado = random.randint(1, 6)
    print(f"\nResultado del dado: {resultado}")

# Simular 100 lanzamientos de una moneda
# Función para lanzar moneda
def lanzar_moneda():
    return random.choice(["cara", "cruz"])

# Procedimiento para lanzar 100 monedas
def experimento_monedas(n=100):
    resultados = {"cara": 0, "cruz": 0} # Diccionario donde se almacenarán los resultados

    # _ se usa como variable anónima cuando no necesitas el valor actual del índice del bucle. Si n=100, se ejecutará 100 veces
    for _ in range(n):
        resultado = lanzar_moneda() # Llama a la función lanzar_moneda() y lo almacena en la variable resultado

        resultados[resultado] += 1 # Según el valor de resultado, incrementa el contador "cara" o "cruz"

    print(f"\nLanzando la moneda {n} veces...\n")
    print(f"Resultados tras {n} lanzamientos:\n{resultados}")

# Experimento de probabilidad (Estimar la probabilidad de que al lanzar dos dados, la suma sea 7)
def suma_siete(n=10000):
    exito = 0

    for _ in range(n):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)

        if dado1 + dado2 == 7:
            exito += 1

    prob = exito / n
    print(f"\nLa probabilidad estimada de obtener 7: {prob:.2f}")

# Función principal
def main():
    while True:
        print("\nNúmeros aleatorios")
        print("==================")
        print("[1] Simular el lanzamiento de un dado")
        print("[2] Simular 100 lanzamientos de moneda")
        print("[3] Experimento de probabilidad")
        print("[0] Salir del programa")
        try:
            op = int(input("\n¿Qué operación desea realizar?: "))
            match op:
                case 1:
                    lanzar_dado()
                case 2:
                    experimento_monedas()
                case 3:
                    suma_siete()
                case 0:
                    break
                    # return
                case _:
                    print("\nEscriba una opción válida")
        except:
            print("\nEscriba un número entero")

main()