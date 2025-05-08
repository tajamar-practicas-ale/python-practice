def es_vocal(letra):
    # Devuelve True si la letra es una vocal (minúscula o mayúscula)
    return letra.lower() in "aeiou"

def analizar_texto(texto):
    print("\n--- Análisis del texto ---")
    print(f"Original: {texto}")
    print(f"Mayúsculas: {texto.upper()}")
    print(f"Minúsculas: {texto.lower()}")
    print(f"Invertido: {texto[::-1]}")
    print(f"Sin espacios: {texto.replace(' ', '')}")
    
    # Contar vocales: sumar 1 por cada carácter que sea vocal
    vocales = sum(1 for c in texto if es_vocal(c))
    
    # Contar consonantes: que sean letras pero no vocales
    consonantes = sum(1 for c in texto if c.isalpha() and not es_vocal(c))
    
    print(f"Número de vocales: {vocales}")
    print(f"Número de consonantes: {consonantes}")
    
    # Reemplazo de caracteres (solo ejemplo estético)
    reemplazado = texto.replace("a", "@").replace("e", "3")
    print(f"Texto con reemplazos: {reemplazado}")

def main():
    texto = input("Ingresa un texto para analizar: ")
    analizar_texto(texto)

if __name__ == "__main__":
    main()
