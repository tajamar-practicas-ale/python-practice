# Las listas son estructuras de datos mutables, lo que quiere decir que pueden ser modificadas
# Las tuplas son estructuras de datos inmutables, no se pueden modificar

lista = ["Hola", 5]
tupla = (True, 54)
otratupla = (69, 21)

def ver():
    print("Lista (mutable): ")
    print(lista)

    print("\nTupla (inmutable): ")
    print(tupla)

def agregar_item():
    item = input("Escribe el item que quieres agregar a la lista: ")

    lista.append(item)

    print("Lista con nuevo item \n")
    print(lista)

def op_tupla():

    global tupla # Usar global para acceder a la variable tupla

    print("Tupla sin concatenar:")
    print(tupla)
    print("\n")
    print("Tupla a concatenar:")
    print(otratupla)

    tupla += otratupla

    print("\nTuplas concatenadas")
    print(tupla)

def main():
    print("Elige la operación que quieres realizar")
    op = input("'-' para visualizar lista y tupla, '+' para agregar un item a la lista y '*' para concatenar tuplas: ")

    match op:
        case '-':
            ver()
        case '+':
            agregar_item()
        case '*':
            op_tupla()

if __name__ == "__main__":
    main()