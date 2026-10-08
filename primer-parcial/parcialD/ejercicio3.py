
# ==========================================
# Ejercicio 3
# ==========================================

"""
El diccionario sistema_previsional tiene cargados para cada país (clave) cuatro datos: cantidad de personas
trabajando, cantidad de personas jubiladas, cantidad de personas desempleadas (todos enteros dados en miles) y
grupo al que pertenece (por ejemplo: "Mercosur", "Unión Europea", etc.).
Se pide que escribas un programa modular (compuesto por funciones) en Python que:

1. Obtenga el diccionario con los datos haciendo uso de la función obtener_datos() que se encuentra en la
librería Datos_Generales. La función devuelve el diccionario. NO debes escribirla.

2. Calcule el promedio mundial de personas que están trabajando, personas jubiladas y personas
desempleadas.

3. Imprima un listado, con los nombres de los países y su tasa de desempleo, y la relación
jubilados/trabajadores. El listado debe estar ordenado de mayor a menor por tasa de desempleo.
Indicando:
    País - Tasa de Desempleo - Relación Jubilados/Trabajadores

4. Genere un nuevo diccionario, donde la clave sea el grupo (por ejemplo "Mercosur", "Unión Europea", etc.) y
los datos asociados sean el total de personas que trabajan, el total de jubilados y el total de desempleados.
"""
#from Datos_Genereales import obtener_datos 

def promedio(sistema_provisional):
    trabajando = 0
    jubilados = 0
    desempleados = 0
    paises = 0
    promedio = [0,0,0]

    for pais in sistema_provisional:
        paises +=1 
        trabajo = sistema_provisional[pais][0]
        jubilado = sistema_provisional[pais][1]
        desempleado = sistema_provisional[pais][2]


        trabajando += trabajo
        jubilados +=  jubilado
        desempleados += desempleado

    promedio[0] = trabajando / paises
    promedio[1] = jubilados / paises
    promedio[2] = desempleados / paises

    return promedio

def tasa_desempleo(sistema_provisional):
    tasa = []
    for pais in sistema_provisional:
        trabajo = sistema_provisional[pais][0]
        jubilado = sistema_provisional[pais][1]
        desempleado = sistema_provisional[pais][2]


        tasa_desempleados = (desempleado / (trabajo + desempleado)) * 100
        relacion = jubilado / trabajo
        tasa.append([pais,tasa_desempleados, relacion])

    ordenados = sorted(tasa, key=lambda x: x[1], reverse = True)
        
    print("País - Tasa de Desempleo - Relación Jubilados/Trabajadores")
    print(ordenados)


def diccionario(sistema_provisional):
    dic = {}

    for pais in sistema_provisional:
        trabajo = sistema_provisional[pais][0]
        jubilado = sistema_provisional[pais][1]
        desempleado = sistema_provisional[pais][2]
        grupo = sistema_provisional[pais][3]

        if grupo not in dic:
            dic[grupo] = [0,0,0]

        dic[grupo][0] += trabajo  # se hacen uno por uno pq si no concatena los resultados
        dic[grupo][1] += jubilado
        dic[grupo][2] += desempleado

    return dic
        

def main():
    sistema_provisional = obtener_Datos()

    promedio_mundial = promedio(sistema_provisional)

    tasa_desempleo(sistema_provisional)

    datos_por_grupo = diccionario(sistema_provisional)


main()