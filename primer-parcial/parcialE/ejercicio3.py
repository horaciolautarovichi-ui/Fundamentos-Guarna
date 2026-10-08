# ==========================================
# Ejercicio 3
# ==========================================

"""
Se cuenta con una lista votacion, ya cargada, que contiene sublistas.
Cada una de esas sublistas tiene los siguientes valores: partido (string), nro. de mesa (entero), diputados (entero), senadores (entero)
Ejemplo: [["PP", 2, 19, 35], ["PSOE", 13, 20, 30], ["VOX", 2, 15, 15], ["PP", 5, 0, 15], ["VOX", 5, 10, 13], ["PP", 13, 9, 5], ...].
Los recuentos son de diferentes mesas por lo que los nombres de los partidos aparecerán varias veces.

Se pide que escribas un programa modular en Python (ccese la lompuesto por funciones), que proista votacion una única
vez y:
1. Obtenga la lista votación invocando a la función obtener_votos de la librería votacion2024.
2. Genere un diccionario con clave partido y valores total_diputados, total_senadores.
3. Imprima un listado de los partidos con el respectivo total de votos obtenidos (diputados + senadores) y el
porcentaje que representa el total de votos obtenidos sobre el total general, ordenados de mayor a menor por el
total de votos obtenidos. El listado debe tener un formato de 3 columnas.
Informe el total de mesas escrutadas.
"""

#from votacion2024 import obtener_votos

def totales(lista_votacion):
    dic = {}
    total_votos = 0
    mesas = 0
    mesas_repetidas = []
    for partido in lista_votacion:

        nombre = partido[0]
        if nombre not in dic:
            dic[nombre] = [0,0]

        mesa = partido[1]
        total_diputados = partido[2]
        total_senadores = partido[3]

        dic[nombre][0] += total_diputados
        dic[nombre][1] += total_senadores
        total_votos += total_senadores + total_diputados
        if mesa not in mesas_repetidas:
            mesas += 1
            mesas_repetidas.append(mesa)

    informe = [dic, total_votos, mesas]
    return informe



def votos(informe):
    dic = informe[0]
    total_votos = informe[1]
    mesas = informe[2]
    listado = []

    print("partido - votos totales - porcentaje")

    for partido in dic:
        disputados = dic[partido][0]
        senadores = dic[partido][1]

        totales = disputados + senadores

        porcentaje = totales/total_votos * 100

        listado.append([partido, totales, porcentaje])
        
        ordenados = sorted(listado, key=lambda x: x[1], reverse = True)
        
        print(ordenados)

    print("=========================")
    print(f"mesas totales{mesas}")





    

def main():
    #lista = obtener_votos()
    informe = totales(lista)
    votos(informe)


main()






        



    



        
    





