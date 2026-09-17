""" 

Ejercicio 1

Escribir una función que reciba una cadena de caracteres que representa un alias bancario. La función deberá devolver True o False, en base a haber evaluado que dicho alias esté bien formado.

Se debe controlar:
a. Que tenga entre 6 y 20 caracteres, pudiendo ser letras, números y caracteres especiales (guión del medio, guión bajo o punto).

b. Que contenga al menos 6 letras y un carácter especial.

c. Que los caracteres especiales no se encuentren ni en la primera, ni la última posición.

RESTRICCIÓN: De los métodos de la clase cadena, sólo se puede usar el método isalpha. Se deben evitar ciclos innecesarios."""


def alias_bancario(alias):

    valido = True

    cant_letras = 0
    caracter_especial = 0

    primer_car = alias[0]
    ultimo_car = alias[-1]

    if len(alias) > 20 or len(alias) < 6:
        valido = False
    else:
        if primer_car in "._-" or ultimo_car in "_-.":
            valido = False

    
    if valido == True:

        while valido and i < len(alias):
                    caracter = alias[i]

                    if caracter.isalpha():
                        cant_letras += 1
                    elif caracter in ".-_":
                        caracter_especial += 1
                    elif caracter < "0" or caracter > "9":
                        valido = False

                    i += 1

        if cant_letras >= 6 and caracter_especial >= 1:
            valido = True

    return valido 

