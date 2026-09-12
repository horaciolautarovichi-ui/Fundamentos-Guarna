"""
En los ejercicios que debas utilizar ciclos, la incorrecta elección del ciclo o el uso incorrecto del mismo, en base a lo explicado en las clases, invalidará el ejercicio por completo.

No se pueden utilizar métodos y/o recursos no explicados en el curso.

En todos los ejercicios se debe cumplir con las prácticas que se explicaron en el curso (nombres, estilos, etc.) y las que se encuentran en el PEP de la cátedra. Además se debe prestar especial atención a la modularización y la eficiencia (no hacer ciclos de más, etc.).

Escribir con letra clara y poner nombre y legajo a todas las hojas."""


import doctest



""" 

Ejercicio 1

Escribir una función que reciba una cadena de caracteres que representa un alias bancario. La función deberá devolver True o False, en base a haber evaluado que dicho alias esté bien formado.

Se debe controlar:
a. Que tenga entre 6 y 20 caracteres, pudiendo ser letras, números y caracteres especiales (guión del medio, guión bajo o punto).

b. Que contenga al menos 6 letras y un carácter especial.

c. Que los caracteres especiales no se encuentren ni en la primera, ni la última posición.

RESTRICCIÓN: De los métodos de la clase cadena, sólo se puede usar el método isalpha. Se deben evitar ciclos innecesarios."""


def alias_bancario(alias):

    valido = False

    primer_car = alias[0]
    ultimo_car = alias[len(alias)-1]

    if len(alias) > 20 or len(alias) < 6:
        valido = False
    else:
        if primer_car in "._-" or ultimo_car in "_-.":
            valido = False


    cant_letras = 0
    caracter_especial = 0

    for caracter in alias:
        if caracter.isalpha():
            cant_letras += 1
        elif caracter in ".-_":
            caracter_especial += 1
        elif caracter < "0" or caracter > "9":
            valido = False

    if cant_letras >= 6 and caracter_especial >= 1:
        valido = True

    return valido 



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


def elegir_comidas(comidas : list, prohibidos:  list) -> list:

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