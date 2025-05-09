def operacion(n1, n2):
    return n1 * n2

def main():
    try:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        resultado = operacion(n1, n2)
        print(f"{n1} * {n2} = {resultado}")
    except:
        print("Ingrese un valor válido")
    finally:
        print("Programa finalizado")

# Ejecutamos la función principal
if __name__ == "__main__":
    main()