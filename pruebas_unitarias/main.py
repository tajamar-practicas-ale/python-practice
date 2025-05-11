def sumar(a, b):
    return a + b

def eliminar_clave(dic, clave):
    if clave in dic:
        del dic[clave]
        return True
    return False

def agregar_elemento_conjunto(conjunto, valor):
    if valor in conjunto:
        return False
    conjunto.add(valor)
    return True