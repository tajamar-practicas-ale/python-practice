from datetime import datetime, timedelta

def obtener_fecha_actual():
    """
    Esta función obtiene la fecha y hora actuales usando `datetime.now()`.
    La fecha y hora actuales se imprimen en consola en su formato por defecto.
    """
    # Obtener la fecha y hora actuales
    ahora = datetime.now()
    print(f"Fecha y hora actuales: {ahora}")

def convertir_cadena_a_fecha(cadena):
    """
    Esta función convierte una cadena que representa una fecha en el formato 'YYYY-MM-DD' a un objeto datetime.
    Utiliza `datetime.strptime()` para convertir la cadena en un objeto datetime.
    
    Args:
    - cadena (str): Una cadena que representa una fecha en formato 'YYYY-MM-DD'.
    
    Imprime la fecha convertida en formato datetime.
    """
    # Convertir una cadena con formato 'YYYY-MM-DD' a un objeto datetime
    fecha = datetime.strptime(cadena, "%Y-%m-%d")
    print(f"Fecha convertida: {fecha}")

def calcular_diferencia_fechas(fecha1, fecha2):
    """
    Esta función calcula la diferencia entre dos fechas. 
    La diferencia se calcula restando un objeto `datetime` de otro, lo cual devuelve un objeto `timedelta`.
    La propiedad `.days` del objeto `timedelta` se utiliza para obtener la diferencia en días.
    
    Args:
    - fecha1 (datetime): La primera fecha.
    - fecha2 (datetime): La segunda fecha.
    
    Imprime la diferencia en días entre ambas fechas.
    """
    # Calcular la diferencia entre dos fechas
    diferencia = fecha2 - fecha1
    print(f"Diferencia entre las fechas: {diferencia.days} días")

def sumar_dias(fecha, dias):
    """
    Esta función suma una cantidad de días a una fecha usando `timedelta`.
    La operación `fecha + timedelta(days=dias)` devuelve una nueva fecha que es el resultado de sumar los días especificados.
    
    Args:
    - fecha (datetime): La fecha a la que se le sumarán los días.
    - dias (int): El número de días que se desean sumar a la fecha.
    
    Imprime la nueva fecha después de sumar los días.
    """
    # Sumar 'dias' a una fecha
    nueva_fecha = fecha + timedelta(days=dias)
    print(f"Fecha después de sumar {dias} días: {nueva_fecha}")

def restar_dias(fecha, dias):
    """
    Esta función resta una cantidad de días a una fecha usando `timedelta`.
    La operación `fecha - timedelta(days=dias)` devuelve una nueva fecha que es el resultado de restar los días especificados.
    
    Args:
    - fecha (datetime): La fecha a la que se le restarán los días.
    - dias (int): El número de días que se desean restar a la fecha.
    
    Imprime la nueva fecha después de restar los días.
    """
    # Restar 'dias' a una fecha
    nueva_fecha = fecha - timedelta(days=dias)
    print(f"Fecha después de restar {dias} días: {nueva_fecha}")

def formatear_fecha(fecha):
    """
    Esta función convierte un objeto `datetime` a una cadena con un formato específico usando `strftime`.
    El formato utilizado en este caso es 'dd-mm-YYYY'.
    
    Args:
    - fecha (datetime): El objeto datetime que se desea formatear.
    
    Imprime la fecha en el formato 'dd-mm-YYYY'.
    """
    # Formatear la fecha en el formato deseado 'dd-mm-YYYY'
    fecha_formateada = fecha.strftime("%d-%m-%Y")
    print(f"Fecha formateada: {fecha_formateada}")

def main():
    """
    Esta es la función principal que llama a las otras funciones para realizar distintas manipulaciones con fechas.
    - Obtiene la fecha y hora actual.
    - Convierte una cadena a un objeto datetime.
    - Calcula la diferencia entre dos fechas.
    - Suma y resta días a una fecha.
    - Formatea una fecha.
    """
    # Obtener la fecha actual
    obtener_fecha_actual()
    
    # Convertir una cadena a fecha
    cadena_fecha = "2025-05-08"
    convertir_cadena_a_fecha(cadena_fecha)
    
    # Calcular la diferencia entre dos fechas
    fecha1 = datetime(2025, 5, 1)
    fecha2 = datetime(2025, 5, 8)
    calcular_diferencia_fechas(fecha1, fecha2)
    
    # Sumar días a una fecha
    fecha = datetime(2025, 5, 8)
    sumar_dias(fecha, 10)
    
    # Restar días a una fecha
    restar_dias(fecha, 5)
    
    # Formatear una fecha
    formatear_fecha(fecha)

if __name__ == "__main__":
    # Ejecutar la función principal
    main()
