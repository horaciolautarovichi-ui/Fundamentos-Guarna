
"""
Ejercicio 3

Se cuenta con una lista salarios, ya cargada, que contiene sublistas, cada una de esas sublistas tiene los siguientes valores: empresa (string), puesto (string), cantidad_de_profesionales (entero), salario_por_profesional (entero en dólares).

Ejemplo:

Python
[["GlobalTek", "Desarrollador", 55, 1800], ["GlobalTek", "Tester", 75, 1300], ["ITSol", "Desarrollador", 44, 1500], ...]
Se pide que escribas un programa modular (compuesto por funciones) en Python que:

Procese esa lista y genere un diccionario con clave: puesto y valores: total_cantidad, total_salarios. La lista con los valores a procesar se obtiene invocando a la función obtener_lista_salarios() de la librería salarios.

Luego, debe mostrar por pantalla, los puestos y su promedio salarial, ordenados de mayor a menor por promedios salariales. La salida debe estar formateada, de forma que se visualice una columna para los puestos, y otra para el promedio salarial.
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




