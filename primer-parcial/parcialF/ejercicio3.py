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


#from datos_generales import obtener_lista_salarios
#va sin parentesis 

def diccionario(lista):

    dic = {}

    for puesto in lista:

        clave = puesto[1]
        salario = puesto[2]


        if clave not in dic:
            dic[clave] = [0,0,0]

        dic[puesto][0] += salario
        dic[puesto][1] += 1
        dic[puesto][2] = salario/dic[puesto][1]
    return dic

def ordenamiento(dic):
    lista = []
    for puesto in dic:
        lista.append([puesto, dic[puesto][2]])

    #ordenamos la lista con lambda

    ordenados = sorted(lista, key=lambda x: x[1], reverse = True)

    return ordenados


def main():
    lista = []
    #obtener_lista_salarios(lista)

    dic = diccionario(lista)

    ordenados = ordenamiento(dic)
    print("puesto - sueldo promedio")
    for trabajo in ordenados:
        print(f"{trabajo[0]}-{trabajo[1]}\n")




