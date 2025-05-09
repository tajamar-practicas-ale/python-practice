def encontrar_maximo_de_tres(a, b, c):
    """
    Esta función determina el mayor de tres números utilizando comparaciones condicionales.
    El flujo lógico sigue un patrón clásico de diagrama de flujo.
    """
    if a > b:
        # Si 'a' es mayor que 'b', ahora comparamos 'a' con 'c'
        if a > c:
            mayor = a  # 'a' es el mayor
        else:
            mayor = c  # 'c' es el mayor
    else:
        # Si 'b' es mayor o igual que 'a', comparamos 'b' con 'c'
        if b > c:
            mayor = b  # 'b' es el mayor
        else:
            mayor = c  # 'c' es el mayor

    return mayor

def main():
    """
    Función principal del programa. Solicita tres números al usuario y muestra el mayor.
    """
    print("Ingrese tres números para encontrar el mayor:")
    
    try:
        a = float(input("Primer número (a): "))
        b = float(input("Segundo número (b): "))
        c = float(input("Tercer número (c): "))
        
        resultado = encontrar_maximo_de_tres(a, b, c)
        
        print(f"El mayor de los tres números es: {resultado}")
    
    except ValueError:
        print("Error: Debes ingresar valores numéricos válidos.")

# función principal
if __name__ == "__main__":
    main()
