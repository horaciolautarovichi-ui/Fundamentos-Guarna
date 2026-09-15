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