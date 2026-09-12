
""" 

Ejercicio 2

Escribir una función elegir_comidas en Python que reciba una lista de listas, cada sublista es una comida, en donde el primer elemento es el nombre de la comida y los siguientes elementos los respectivos ingredientes. También recibe una lista de ingredientes prohibidos. Debe devolver una lista con los nombres de las comidas permitidas (no deben contener ingredientes prohibidos).

Ejemplo:

Python
comidas = [
    ["milanesa", "bifes de nalga", "pan rallado", "huevo"],
    ["ravioles", "harina", "espinaca", "ricota"],
    ["pizza", "queso", "harina", "tomate", "aceitunas"],
]
prohibidos_1 = ["huevo", "nueces", "aceitunas"]
prohibidos_2 = ["huevo", "nueces"]

elegir_comidas(comidas, prohibidos_1)  # --> ['ravioles']
elegir_comidas(comidas, prohibidos_2)  # --> ['ravioles', 'pizza']
Testea la función usando doctest, para 2 listas de comidas de al menos 4 comidas cada una; y 3 listas de ingredientes prohibidos, con al menos 2 ingredientes cada una. Generá 4 casos de prueba diferentes."""


def elegir_comidas(comidas ,prohibidos):

    # Modulo doctest para verificar los casos de prueba requeridos por la consigna
    """
    >>> comidas_1 = [
    ...     ["milanesa", "bifes de nalga", "pan rallado", "huevo"],
    ...     ["ravioles", "harina", "espinaca", "ricota"],
    ...     ["pizza", "queso", "harina", "tomate", "aceitunas"],
    ...     ["ensalada", "lechuga", "tomate", "aceite"]
    ... ]

    >>> comidas_2 = [
    ...     ["tarta", "harina", "acelga", "huevo"],
    ...     ["sopa", "agua", "verduras", "sal"],
    ...     ["pastel de papa", "papa", "carne", "cebolla", "huevo"],
    ...     ["empanadas", "harina", "carne", "aceitunas"]
    ... ]

    >>> prohibidos_1 = ["huevo", "nueces", "aceitunas"]
    >>> prohibidos_2 = ["carne", "sal"]
    >>> prohibidos_3 = ["azucar", "mani"]

    Caso 1: Usando comidas_1 con prohibidos_1
    >>> elegir_comidas(comidas_1, prohibidos_1)
    ['ravioles']

    Caso 2: Usando comidas_1 con prohibidos_2
    >>> elegir_comidas(comidas_1, prohibidos_2)
    ['milanesa', 'ravioles', 'pizza', 'ensalada']

    Caso 3: Usando comidas_2 con prohibidos_1
    >>> elegir_comidas(comidas_2, prohibidos_1)
    ['sopa']

    Caso 4: Usando comidas_2 con prohibidos_2
    >>> elegir_comidas(comidas_2, prohibidos_2)
    ['tarta']
    """ 

    permitidas = []

    for comida in comidas: ## recorremos cada fila de comidas en comida

        nombre = comida[0]

        ingredientes = comida[1:] ## lo usamos para recorrer desde el indice uno hasta el final

        es_permitida = True

        i = 0

        while i < len(ingredientes) and es_permitida: ## mientras i sea menor a la cantidad de ingredientes y es_permitida == True seguimos

            if ingredientes[i] in prohibidos: ## si en algun momento el ingrediente esta en prohibidos cortamos el bucle y pasamos a la otra comida del for
                es_permitida = False
            i += 1

        if es_permitida == True:
            permitidas.append(nombre )          

    return permitidas



def main():

    # Ejecuta automáticamente las pruebas especificadas en la docstring
    print(doctest.testmod)