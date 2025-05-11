import os

# Procedimiento para ver el directorio actual
def ver_directorio_actual():
    print(f"\nDirectorio actual: {os.getcwd()}")

# Procedimiento para listas los archivos y carpetas
def listar_archivos():
    print("\nArchivos y carpetas:")
    for item in os.listdir():
        print("  -", item)

# Procedimiento para cambiar de directorio ("../" para regresar al anterior)
def cambiar_directorio():
    nuevo_dir = input("\nIngresa la ruta del nuevo directorio: ")
    if os.path.isdir(nuevo_dir):
        os.chdir(nuevo_dir)
        print("Directorio cambiado.")
    else:
        print("Ruta no válida.")

# Procedimiento para crear un archivo
def crear_archivo():
    nombre = input("\nNombre del archivo a crear: ")
    contenido = input("Escribe el contenido del archivo:\n")
    with open(nombre, "w") as f:
        f.write(contenido)
    print(f"Archivo '{nombre}' creado.")

# Procedimiento para leer un archivo
def leer_archivo():
    nombre = input("\nNombre del archivo a leer: ")
    if os.path.isfile(nombre):
        with open(nombre, "r") as f:
            print("\nContenido del archivo:")
            print(f.read())
    else:
        print("Archivo no encontrado.")

# Menú
def main():
    while True:
        print("\n=== Menú de Operaciones con OS ===")
        print("[1] Ver directorio actual")
        print("[2] Listar archivos y carpetas")
        print("[3] Cambiar de directorio")
        print("[4] Crear archivo")
        print("[5] Leer archivo")
        print("[0] Salir")

        opcion = input("Selecciona una opción: ")

        match opcion:
            case "1":
                ver_directorio_actual()
            case "2":
                listar_archivos()
            case "3":
                cambiar_directorio()
            case "4":
                crear_archivo()
            case "5":
                leer_archivo()
            case "0":
                print("\nSaliendo del programa.")
                break
            case _:
                print("\nOpción no válida. Intenta de nuevo.")

# Ejecutar menú
main()
