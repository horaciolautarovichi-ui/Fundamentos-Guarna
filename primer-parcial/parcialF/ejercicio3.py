# ==========================================
# Ejercicio 3
# ==========================================

"""
Se cuenta con una lista salarios, ya cargada, que contiene sublistas, cada una de esas sublistas tiene los siguientes
valores: empresa (string), puesto (string), salario (entero).
Ejemplo:
[["Globant", "Desarrollador", 1000], ["Globant", "Tester", 800], ["Accenture", "Desarrollador", 920], ...]

Se pide que escribas un programa modular (compuesto por funciones) en Python que:

1. procese esa lista y genere un diccionario con clave: puesto y valores: total_salarios, cantidad, salario_promedio.
La lista con los valores a procesar se obtiene invocando a la función obtener_lista_salarios().

2. Luego, debe mostrar por pantalla, los puestos y su promedio salarial, ordenados de mayor a menor por
promedios salariales. La salida debe estar formateada, de forma que se visualice una columna para los puestos, y
otra para el promedio salarial.
"""