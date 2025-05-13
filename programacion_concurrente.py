import threading
import time

def tarea(nombre):
    print(f"Inicio de {nombre}")
    time.sleep(2)
    print(f"Fin de {nombre}")

# threading.Thread: crea un hilo (tarea que se ejecuta en paralelo)
hilo1 = threading.Thread(target=tarea, args=("Tarea 1",))
hilo2 = threading.Thread(target=tarea, args=("Tarea 2",))

# start() inicia la ejecución del hilo
hilo1.start()
hilo2.start()

# join() espera a que ese hilo termine antes de continuar
hilo1.join()
hilo2.join()

print("Ambas tareas han terminado.")