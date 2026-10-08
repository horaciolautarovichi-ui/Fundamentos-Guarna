
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
#from salarios import obtener_lista_salarios()
def totales(salarios):
    
    dic = {}
    for puesto in salarios:
        nombre_puesto = puesto[1]

        if nombre_puesto not in dic:
            dic[nombre_puesto] = [0,0]

            trabajadores = puesto[2]
            sueldo = puesto[3]

            dic[nombre_puesto][0] += trabajadores
            dic[nombre_puesto][1] += sueldo

    return dic

def promedio(dic):

    print("puesto - promedio salarial")
    lista = []
    
    for puesto in dic:
        total = dic[puesto][0]
        sueldo = dic[puesto][1] #faltaria 
        promedio = sueldo/total

        lista.append([puesto, promedio])

    ordenado = sorted(lista, key=lambda x: x[1], reverse = True)
    print(ordenado[0],"-", ordenado[1])
        







        







