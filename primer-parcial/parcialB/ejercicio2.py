# ==========================================
# Ejercicio 2
# ==========================================

"""
Escribir una función elegir_comidas en Python que recibe una lista de listas, cada sublista es una comida, en donde el
primer elemento es el nombre de la comida y los siguientes elementos los respectivos ingredientes. También recibe
una lista de ingredientes prohibidos. Debe devolver una lista con los nombres de las comidas permitidas (no deben
contener ingredientes prohibidos).

Ejemplos:
    comidas = [ ["milanesa", "bifes de nalga", "pan rallado", "huevo"],
                ["ravioles", "harina", "espinaca", "ricota"],
                ["pizza", "queso", "harina", "tomate", "aceitunas"] ]
    prohibidos_1 = ["huevo", "nueces", "aceitunas"]
    prohibidos_2 = ["huevo", "nueces"]
    elegir_comidas(comidas, prohibidos_1) ---> ["ravioles"]
    elegir_comidas(comidas, prohibidos_2) ---> ["ravioles", "pizza"]
"""

def elegir_comidas(comidas, prohibidos):

    permitidas = []
   

    for comida in comidas:

        i = 1 #desde 1 ya q el 0 siempre es el nombre
        es_permitida = True #dentro del for ya q por cada vuelta hay q ponerlo en permitido para q entre al while

        while es_permitida and i < len(comida):
            if comida[i] in prohibidos:
                es_permitida = False
            i += 1
        if es_permitida == True:
            permitidas.append(comida[0])

    return permitidas



