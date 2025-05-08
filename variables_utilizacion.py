x = 10 # variable global

def funcion_externa():
    x = 20 # crea una variable local

    def funcion_interna():
        nonlocal x # hace referencia a la x de la funcion_externa
        x = 30 # modifica la variable en la funcion_interna
        global y # define la variable como global

        y = 15 # modifica la variable global y
    funcion_interna()
    print(f"Dentro de la función externa x = {x}") # salida 30

funcion_externa()
print(f"Variable global x = {x}") # salida 10
print(f"Variable global y = {y}") # salida 15