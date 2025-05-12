class Perro:
    # Constructor (__init__) - se usa para inicializar los atributos del objeto
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre  # Atributo
        self.raza = raza      # Atributo
        self.edad = edad      # Atributo

    # Método (comportamiento) de la clase
    def ladrar(self):
        print(f"{self.nombre} dice ¡Guau!")

    # Otro método
    def descripcion(self):
        print(f"{self.nombre} es un {self.raza} de {self.edad} años.")
        
# Crear objetos (instancias) de la clase Perro
perro1 = Perro("Rex", "Pastor Alemán", 3)
perro2 = Perro("Luna", "Bulldog", 5)

# Llamar a métodos de los objetos
perro1.ladrar()
perro2.ladrar()

perro1.descripcion()
perro2.descripcion()
