semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

def agregar():
    item = str(input("¿Qué elemento desea agregar a la lista?: "))

    semana.append(item)

    print("\n¡Elemento añadido exitosamente!")
    print(semana)

def acceso():
    print("Lista de la semana:")
    for i, dia in enumerate(semana):
        print(f"{i}: {dia}")

    # Solicitar al usuario un índice
    try:
        indice = int(input("Escribe el número del índice del día que quieres ver: "))

        # Verificar si el índice está dentro del rango
        if 0 <= indice < len(semana):
            print(f"Día seleccionado: {semana[indice]}")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Por favor, escribe un número válido.")

def modificar():
    print("Lista de la semana:")
    for i, dia in enumerate(semana):
        print(f"{i}: {dia}")

    # Solicitar al usuario un índice
    try:
        indice = int(input("Escribe el número del índice del día que quieres modificar: "))

        # Verificar si el índice está dentro del rango
        if 0 <= indice < len(semana):
            cambio = input(f"Escribe el valor por el que quieres cambiar {semana[indice]}: ")
            semana[indice] = cambio

            print("Lista de la semana:")
            for i, dia in enumerate(semana):
                print(f"{i}: {dia}")
        else:
            print("Índice fuera de rango.")

    except ValueError:
        print("Por favor, escribe un número válido.")

def recorrer():
    print("Lista de la semana:")
    for i, dia in enumerate(semana):
        print(f"{i}: {dia}")

def main():
    op = input("¿Qué operación deseas realizar?\n'+' para agregar un elemento, '-' para ver un elemento en específico, '*' Para modificar un elemento y '/' para recorrer la lista completa: ")

    match op:
        case '+':
            agregar()
        case '-':
            acceso()
        case '*':
            modificar()
        case '/':
            recorrer()

if __name__ == "__main__":
    main()