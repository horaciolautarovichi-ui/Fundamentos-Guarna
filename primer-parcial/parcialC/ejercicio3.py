
# ==========================================
# Ejercicio 3
# ==========================================

"""
3) Se cuenta con una lista salarios, ya cargada, que contiene sublistas, cada una de esas sublistas tiene los
siguientes valores: puesto (string), salario (entero). Los puestos pueden estar repetidos. Ejemplo:
[["Desarrollador", 1000], ["Tester", 800], ["Desarrollador", 920], ...]. Los datos surgen de diferentes
empresas por eso las repeticiones.

Se pide que escribas un programa en Python que procese esa lista y genere un diccionario con clave
puesto y valores total_salarios, cantidad, promedio.

Luego, debe listar los puestos - promedios, ordenados de mayor a menor por promedios salariales.
"""


def obtener_lista_salarios(salarios):


    resultado = {} ##declaramos el diccionario resultado donde se almacena la info final

    for salario in salarios: ##recorremos todos los puestos 

        puesto = salario[1]
        cantidad = salario[2]
        sueldo = salario[3]

        if puesto in resultado: ##si el puesto ya esta cargado sumamos la info
            resultado[puesto][0] += cantidad
            resultado[puesto][1] += cantidad * sueldo
        else: ## sino lo creamos con la info del puesto actual
            resultado[puesto] = [cantidad, cantidad * sueldo]

    return resultado

