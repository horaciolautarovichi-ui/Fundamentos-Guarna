"""
Ejercicio 3

Escribir un programa modular (compuesto por funciones) en Python que resuelva la siguiente problemática de gestión de infracciones de velocidad del centro de monitoreo de multas:

PROCESAMIENTO DE DATOS: Obtener la lista con los datos de infracciones a procesar mediante la función obtener_infracciones() que pertenece a la librería peajes. Cada elemento de esta lista es una sublista que representa una infracción detectada y contiene tres valores; (1) La patente (string), (2) La velocidad registrada (entero), y (3) El valor de la multa (flotante). Una misma patente puede repetirse si cometió más de una infracción. Procesar la lista y generar un diccionario llamado multas_por_patente. Este diccionario deberá tener como clave la patente del vehículo, y como valores: la velocidad máxima alcanzada por esa patente, la cantidad total de multas recibidas y el total acumulado en dinero de las multas.

ANÁLISIS DE RENDIMIENTO: Informar la o las patentes que alcanzaron la mayor velocidad registrada en el sistema. No se pueden ordenar los datos para este paso y la estructura de datos sólo puede ser recorrida una única vez para obtener los resultados.

INFORME DE VENTAS: Mostrar por pantalla de mayor a menor las patentes según el total acumulado en multas. Los datos deben presentarse prolijamente en tres columnas: una para la patente, otra para la cantidad total de multas y la última para el total de dinero acumulado en multas.
"""
#from peajes import obtener_infracciones

def diccinario(lista):
    dic = {}
    for multa in lista:
        patente = multa[0]
        velocidad = multa[1]
        valor = multa[2]

        if patente not in dic:
            dic[patente] = [0,0,0]

        if velocidad > dic[patente][0]:
            dic[patente][0] = velocidad
            velocidad = dic[patente][0]

        dic[patente][1] += 1
        dic[patente][2] += valor
    return dic

def mayor_velocidad(dic):
    lista = []
    actual = 0

    for vehiculo in dic:
        if dic[vehiculo][0] > actual:
            actual = dic[vehiculo][0]
            lista = [vehiculo]
        elif dic[vehiculo][0] == actual:
            lista.append(vehiculo)
    return lista


def ordenamiento(dic):
    lista = []

    for vehiculo in dic:
        multas = dic[vehiculo][1]
        total = dic[vehiculo][2]

        lista.append([vehiculo, multas, total])

    ordenada = sorted(lista, key=lambda x : x[2])

    return ordenada

def main():
    lista = [] #tendramos q usar obtener_infracciones pero para que no se rompa el codigo dejamos asi

    multas_por_patente = diccinario(lista)

    patentes = mayor_velocidad(multas_por_patente)

    print("los vehiculos con mayor velocidad:")

    for patente in patentes:
        print(f"{patente}")

    ordenados = ordenamiento(multas_por_patente)

    print("patente - cant multas - total acumulado")

    for p in ordenados:
        print(f"{p[0]} - {p[1]} - {p[2]}")

main()

