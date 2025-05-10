# Diccionarios, colección de pares clave-valor
persona = {"nombre": "Juan", "edad": 30}

# Conjuntos, colección de elementos únicos y no ordenados
numeros = {1, 2, 3}
pares = {2, 4, 6, 8}
impares = {1, 3, 5, 7}

# Operaciones con Diccionarios
# Recorre el diccionario
def ver_diccionario():
    print("\nDiccionario: ")
    for clave, valor in persona.items():
        print(f"{clave}: {valor}")
    
    print("\n")
    # main()

# Agregar o modificar un valor (Sobreescribe si ya existe)
def agregar_item_dict():
    ver_diccionario()

    clave = input("Escribe la clave que quieres agregar o modificar: ")
    valor = input("Escribe el valor que quieres agregar o modificar: ")
    
    # Agregar una sola clave-valor al diccionario
    persona[clave] = valor

    """
    Agregar varias claves-valor

    persona.update({clave: valor, "ejemplo": "ejemplo"})
    """
    """
    Agregar clave-valor solo si no existe

    persona.setdefault("edad", 30)    # Añade 'edad': 30s
    """    

    print("\nItem agregado o modificado correctamente\n")
    ver_diccionario()
    # main()

# Verificar si la clave existe en el diccionario (True o False)
def verificar_clave():
    clave = input("Escriba la clave que desea verificar: ")

    if clave in persona:
        print(f"\nLa clave {clave} si existe en el diccionario")
        
    else:
        print(f"\nLa clave {clave} no existe en el diccionario\n")
    ver_diccionario()
    # main()

# Eliminar una clave
def del_clave():
    ver_diccionario()

    while True: 
        clave = input("Escribe la clave que deseas eliminar: ")

        if clave in persona:
            del persona[clave]
            print(f"Clave {clave} eliminada correctamente")
            break
            # main()
        else:
            print("\nEscriba una clave válida\n")

# Operaciones con Conjuntos
# Recorrer el conjunto números
def ver_conj_numeros():
    print("\nConjunto números:")
    for num in numeros:
        print(f"{num}")
    print("\n")

# Ver los conjuntos par e impares
def ver_par_impar():
    print("\nConjuntos pares e impares")
    print(f"pares = {pares}")
    print(f"impares = {impares}")
    print("\n")

# Agregar elemento al conjunto números
def agregar_elemento():
    ver_conj_numeros()

    while True:
        try:
            item = int(input("Escriba el número que desee agregar al conjunto: "))

            if item in numeros:
                print("\nNo se permite elementos duplicados en un conjunto.\n")
            else:
                numeros.add(item)
                print("\nNúmero agregado correctamente\n")
                break
        except:
            print("\nDebes ingresar un número entero\n")

# Verificar elemento en el conjunto números
def verificar_conj_nume():
    while True:
        try:
            item = int(input("Escriba el número que desee verificar: "))

            if item in numeros:
                print(f"\nEl número {item} si existe en el conjunto números")
            else:
                print(f"\nEl número {item} no existe en el conjunto números")
            ver_conj_numeros()
            break
        except:
            print("\nDebes ingresar un número entero\n")
    

# Eliminar elemento de un conjunto
def eliminar_nume():
    ver_conj_numeros()

    while True:
        try:
            item = int(input("Escriba el número que desee eliminar: "))

            if item in numeros:
                numeros.remove(item)
                print("\nNúmero eliminado correctamente\n")
                break
            else:
                print("\nEscriba un número válido\n")
        except:
            print("\nDebes ingresar un número entero válido\n")

# Operaciones de conjuntos
def operaciones_conj():
    ver_par_impar()

    # Unión
    print("Unión: pares | impares")
    print(pares | impares)

    # Intersección (Los compara y devuelve los elementos que coinciden)
    print("\nIntersección: pares & {4, 5, 6}")
    print(pares & {4, 5, 6})

    # Diferencia (Los compara y devuelve los elementos que no coinciden)
    print("\nDiferencia: pares - {4, 6}")
    print(pares - {4, 6})

    print("\n")

# Función principal
def main():
    # Bucle while para evitar recursión (Evitar crear un call stack)
    while True:
        print("¿Deseas ver Diccionarios o Conjuntos?")

        try:
            select = int(input("[1] Diccionarios, [2] Conjuntos, [0] Salir: "))

            match select:
                case 1:
                    while True:
                        print("\nDICCIONARIOS")
                        print("============\n")
                        print("[1] Ver Diccionario")
                        print("[2] Agregar o modificar una clave-valor")
                        print("[3] Eliminar clave")
                        print("[4] Verificar si una clave existe")
                        print("[5] Regresar al menú principal")
                        print("[0] Salir\n")
                        try:
                            op = int(input("¿Qué operación deseas realizar?: "))

                            match op:
                                case 1:
                                    ver_diccionario()
                                case 2:
                                    agregar_item_dict()
                                case 3:
                                    del_clave()
                                case 4:
                                    verificar_clave()
                                case 5:
                                    print("\nRegresando al menú principal...\n")
                                    break # Detiene el bucle actual
                                case 0:
                                    print("\nSaliendo del programa...\n")
                                    return # Sale de la función
                                case _:
                                    print("\nEscriba una opción válida\n")
                        except:
                            print("\nDebe ingresar un número entero válido\n")
                case 2:
                    while True:
                        print("\nCONJUNTOS")
                        print("============\n")
                        print("[1] Ver conjunto números")
                        print("[2] Agregar un elemento")
                        print("[3] Eliminar elemento")
                        print("[4] Verificar si un elemento existe")
                        print("[5] Ver operaciones de conjuntos")
                        print("[6] Regresar al menú principal")
                        print("[0] Salir\n")
                        try:
                            op = int(input("¿Qué operación deseas realizar?: "))

                            match op:
                                case 1:
                                    ver_conj_numeros()
                                case 2:
                                    agregar_elemento()
                                case 3:
                                    eliminar_nume()
                                case 4:
                                    verificar_conj_nume()
                                case 5:
                                    operaciones_conj()
                                case 6:
                                    print("\nRegresando al menú principal...\n")
                                    break # Detiene el bucle actual
                                case 0:
                                    print("\nSaliendo del programa...\n")
                                    return # Sale de la función
                                case _:
                                    print("\nEscriba una opción válida\n")
                        except:
                            print("\nDebe ingresar un número entero válido\n")
                            
                case 0:
                    print("\nSaliendo del programa...\n")
                    return # Sale de la función
                case _:
                    print("\nEscriba una opción válida\n")
        except:
            print("\nDebe ingresar un número entero\n")

# Ejecutamos función principal (No se ejecuta cuando es importado en otro archivo)
if __name__ == "__main__":
    main()