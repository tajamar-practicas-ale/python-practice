"""
En C, feof() se usa para verificar si se ha llegado al final de un archivo.
En Python, la forma más común de hacerlo es 
leyendo el fichero línea por línea o usando un bucle que se detenga 
cuando ya no haya más contenido.
"""

# Función para escribir en un fichero
def escribir_en_fichero():
    """
    Esta función abre un fichero en modo escritura ('w') y escribe varias líneas de texto en él.
    Si el fichero ya existe, se sobrescribe su contenido.
    """
    with open("ejemplo.txt", "w") as f:  # 'w' abre el archivo para escribir (sobrescribe si ya existe)
        f.write("Primera línea de texto.\n")
        f.write("Segunda línea de texto.\n")
        f.write("Tercera línea de texto.\n")
    print("Fichero escrito correctamente.")

# Función para leer un fichero
def leer_fichero():
    """
    Esta función abre un fichero en modo lectura ('r') y lee todo su contenido.
    """
    try:
        with open("ejemplo.txt", "r") as f:  # 'r' abre el archivo solo para leer
            contenido = f.read()  # Lee todo el contenido del fichero
        print("Contenido del fichero:")
        print(contenido)
    except FileNotFoundError:
        print("El fichero no existe.")

# Función para recorrer un fichero secuencialmente
def recorrer_fichero():
    """
    Esta función abre un fichero en modo lectura y recorre cada línea del fichero secuencialmente.
    Utiliza un bucle para leer cada línea.
    """
    try:
        with open("ejemplo.txt", "r") as f:  # 'r' abre el archivo solo para leer
            print("Leyendo el fichero línea por línea:")
            for linea in f:  # Lee el fichero línea por línea
                print(linea, end="")  # 'end=""' para evitar que se añadan nuevas líneas innecesarias
    except FileNotFoundError:
        print("El fichero no existe.")

# Función para comprobar el fin de archivo (equivalente a feof en C)
def comprobar_fin_fichero():
    """
    Esta función simula el comportamiento de `feof` de C, para indicar si hemos llegado al fin de un fichero.
    En Python, no existe un equivalente directo a `feof`, pero podemos comprobar si hemos llegado al final del fichero
    al intentar leer más allá del contenido disponible.
    """
    try:
        with open("ejemplo.txt", "r") as f:
            print("\nComprobando fin del fichero: ")
            while True:
                linea = f.readline()  # Lee una línea
                if not linea:  # Si no hay más contenido (equivalente a feof)
                    print("Fin del fichero alcanzado.")
                    break
                print(linea, end="")  # Imprime la línea si aún hay contenido
    except FileNotFoundError:
        print("El fichero no existe.")

# Función principal que llama a las funciones anteriores
def main():
    # Escribir en el fichero
    escribir_en_fichero()
    
    # Leer todo el contenido del fichero
    leer_fichero()
    
    # Recorrer el fichero línea por línea
    recorrer_fichero()
    
    # Comprobar el fin de archivo (feof)
    comprobar_fin_fichero()

if __name__ == "__main__":
    # Ejecutar la función principal
    main()
