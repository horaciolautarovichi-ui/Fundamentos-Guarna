# ==========================================
# Ejercicio 3
# ==========================================

"""
Escribí un programa compuesto por funciones en Python que:

1. Procese una lista de listas, con datos de partidos de fútbol y genere un diccionario "campeonato".
La lista "partidos" contiene sublistas con tres valores: el primer y segundo valor son los nombres de los
equipos, y el tercer valor podrá ser: 0 ó 1 para indicar la posición del equipo ganador, ó 2 para indicar
empate. Los nombres de los equipos pueden repetirse. El diccionario "campeonato" deberá tener por
clave el nombre del equipo, y como valor, una terna compuesta por: partidos ganados (primer valor),
partidos perdidos (segundo valor), partidos empatados (tercer valor).

2. Informe el o los equipos con más partidos jugados.

3. Muestre por pantalla de mayor a menor los equipos con sus puntajes, teniendo en cuenta que por cada
partido ganado se obtienen 3 puntos, y un punto por cada partido empatado. Los datos deben mostrarse
en dos columnas una para el equipo y otra para el puntaje.
"""

def diccionario(lista):
    dic = {}
    for partido in lista:
        nombre_1 = partido[0]
        nombre_2 = partido[1]

        if nombre_1 not in dic:
            dic[nombre_1] = [0,0,0]
        if nombre_2 not in dic:
            dic[nombre_2] = [0,0,0]

        if partido[2] == 0:
            dic[nombre_1][0] += 1
            dic[nombre_2][1] += 1
        elif partido[2] == 1:
            dic[nombre_1][1] += 1
            dic[nombre_2][0] += 1              
        else:
            dic[nombre_1][2] += 1
            dic[nombre_2][2] += 1               
    return dic

def informe(dic):
    equipos = []
    actual = 0
    for equipo in dic:
        ganados = dic[equipo][0]
        perdidos = dic[equipo][1]
        empatados = dic[equipo][2]

        suma = ganados + perdidos + empatados

        if suma > actual:
            actual = suma
            equipos = []
            equipos.append(equipo)
        elif suma == actual:
            equipos.append(equipo)

    return equipos


def puntaje(dic):
    lista = []

    for equipo in dic:
        g = dic[equipo][0] * 3
        e = dic[equipo][2]

        puntaje = g + e
        lista.append([equipo, puntaje])

    ordenados = sorted(lista, key=lambda x : x[1], reverse = True)

    return ordenados


def main():
    lista = []
    #lista de los equipos
    dic = diccionario(lista)
    partidos_equipos = informe(dic)

    print("equipos con mas partidos")
    for equipo in partidos_equipos:
        print(equipo)

    ordenados = puntaje(dic)

    print("equipo  puntaje:")

    for equipo in ordenados:
        print(f"{equipo[0]}    {equipo[1]}")


main()


