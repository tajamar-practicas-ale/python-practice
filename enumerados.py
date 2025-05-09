from enum import Enum
    
class Dias(Enum):
    Lunes = 1
    Martes = 2
    Miercoles = 3
    Jueves = 4
    Viernes = 5
    Sabado = 6
    Domingo = 7

def mostrar(dia):
    if dia == Dias.Lunes:
        print(f"Hoy es {dia.name.lower()}, inicio de semana")
    elif dia == Dias.Domingo:
        print(f"Hoy es {dia.name.lower()}, día de descanso")
    else:
        print(f"Hoy es {dia.name.lower()}")

mostrar(Dias.Domingo)