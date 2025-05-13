# Clase general con método "hablar" definido como plantilla
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "Este animal no hace sonido."

# Subclases que heredan "Animal" y sobreescriben el método hablar
class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Guau!"

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Miau!"

# Al recorrer animales, no importa si es Perro o Gato, se llama hablar() y cada objeto responde según su clase.
animales = [Perro("Firulais"), Gato("Michi"), Animal("Criatura")]
for animal in animales:
    print(animal.hablar())