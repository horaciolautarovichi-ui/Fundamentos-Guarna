"""
Ejercicio 3

Escribí un programa modular (compuesto por funciones) en Python que resuelva la siguiente problemática de gestión de tránsito y recaudación de una estación de peaje:

PROCESAMIENTO DE DATOS: Obtener la lista con los datos de pases a procesar mediante la función obtener_peaje() que pertenece a la librería peajes. Cada elemento de esta lista es una sublista que representa un pase y contiene tres valores: (1) La patente (string), (2) El tipo de vehículo (string: "auto", "moto", "camion", "colectivo", "utilitario", "ambulancia", etc.), y (3) El monto abonado (flotante). Los tipos de vehículo se repiten a lo largo de la lista y no están limitados a una cantidad fija. Procesar la lista y generar un diccionario llamado catalogo_vehiculos. Este diccionario deberá tener como clave el tipo de vehículo, y como valores: la cantidad total de pasadas registradas y el total recaudado por ese tipo de vehículo.

ANÁLISIS DE RENDIMIENTO: Informar el o los tipos de vehículos que tuvieron la menor cantidad de pasadas. No se pueden ordenar los datos para este paso y la estructura de datos sólo puede ser recorrida una única vez para obtener los resultados.

INFORME DE VENTAS: Mostrar por pantalla en forma ascendente los tipos de vehículos según el total recaudado. Los datos deben presentarse prolijamente en tres columnas: una para el tipo de vehículo, otra para la cantidad de pasadas y la última para el total recaudado.
"""

#from peajes import obtener_peajes

def diccionario(lista):
    dic = {}

    for vehiculo in lista:
        tipo = vehiculo[1]
        monto = vehiculo[2]

        if tipo not in dic:
            dic[tipo] = [0,0]

        dic[tipo][0] += 1
        dic[tipo][1] += monto

    return dic

def menor_pasadas(dic):

    lista = []
    menor_tipo = list(dic.keys())[0] #tomamos el primer vehiculo como menor para comparar
    for vehiculo in dic:
        actual = dic[vehiculo][0]
        if actual < dic[menor_tipo][0]:
            menor_tipo = vehiculo
            lista = [menor_tipo]
        elif actual == dic[menor_tipo][0]:
            lista.append(vehiculo)
    return lista

def mostar_pasadas(lista):
    print("el o los vehiculos con menos pasadas fueron:")
    for vehiculo in lista:
        print(f"{vehiculo}")


def ordenamiento(dic):
    lista = []
    for vehiculo in dic:
        monto = dic[vehiculo][1]
        pasadas = dic[vehiculo][0]

        lista.append([vehiculo, pasadas, monto])

    ordenada = sorted(lista, key=lambda x : x[2], reverse=True)

    return ordenada

def mostar_monto(lista):
    print(f"vehiculo - pasadas - monto")

    for vehiculo in lista:
        print(f"{vehiculo[0]} - {vehiculo[1]} - {vehiculo[2]}")

def main():
    lista = [] #utilizariamos la funcion obtener_peajes
    catalogo_vehiculos = diccionario(lista)
    pasada = menor_pasadas(catalogo_vehiculos)
    ordenado = ordenamiento(catalogo_vehiculos)

    mostar_pasadas(pasada)
    mostar_monto(ordenado)


main()
