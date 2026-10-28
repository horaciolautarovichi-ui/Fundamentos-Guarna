"""
Ejercicio 3

Escribí un programa modular (compuesto por funciones) en Python que resuelva la siguiente problemática de gestión de tránsito y recaudación de una estación de peaje:

PROCESAMIENTO DE DATOS: Obtener la lista con los datos de pases a procesar mediante la función obtener_peaje() que pertenece a la librería peajes. Cada elemento de esta lista es una sublista que representa un pase y contiene tres valores: (1) La patente (string), (2) El tipo de vehículo (string: "auto", "moto", "camion", "colectivo", "utilitario", "ambulancia", etc.), y (3) El monto abonado (flotante). Los tipos de vehículo se repiten a lo largo de la lista y no están limitados a una cantidad fija. Procesar la lista y generar un diccionario llamado catalogo_vehiculos. Este diccionario deberá tener como clave el tipo de vehículo, y como valores: la cantidad total de pasadas registradas y el total recaudado por ese tipo de vehículo.

ANÁLISIS DE RENDIMIENTO: Informar el o los tipos de vehículos que tuvieron la menor cantidad de pasadas. No se pueden ordenar los datos para este paso y la estructura de datos sólo puede ser recorrida una única vez para obtener los resultados.

INFORME DE VENTAS: Mostrar por pantalla en forma ascendente los tipos de vehículos según el total recaudado. Los datos deben presentarse prolijamente en tres columnas: una para el tipo de vehículo, otra para la cantidad de pasadas y la última para el total recaudado.
"""

