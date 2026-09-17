# ==========================================
# Ejercicio 1
# ==========================================


"""
Escribir una función contar_caracteres_distintos que reciba una cadena de caracteres y devuelva un entero con la
cantidad de caracteres alfabéticos diferentes sin distinguir mayúsculas de minúsculas ni vocales con tilde. Los dígitos y
símbolos, se me descartan. Agregar las pruebas utilizando la librería doctest con los siguientes ejemplos:

contar_caracteres_distintos("Aaaáb")         devuelve: 2 porque cuenta la "a" y la "b"
contar_caracteres_distintos("Aprobé-con-7")  devuelve: 8 porque cuenta A-p-r-o-b-e-c-n
contar_caracteres_distintos("123$-1")        devuelve: 0 porque no hay caracteres alfabéticos
contar_caracteres_distintos("AmMimmo8")      devuelve: 4 porque cuenta A-m-i-o
"""
import doctest

def contar_caracteres_distintos(caracteres):

    """
    >>> contar_caracteres_distintos("Aaaáb)
    2
    >>> contar_caracteres_distintos("Aprobé-con-7")
    8
    >>> ontar_caracteres_distintos("123$-1")
    0
    >>> contar_caracteres_distintos("AmMimmo8") 
    4
    """

    repetidos = [] ##declaro una lista vacia donde voy a poner los caracteres repetidos 

    distintos = 0

    for caracter in caracteres:
        caracter = caracter.lower()


        if caracter == "á":
            caracter = "a"
        elif caracter == "é":
            caracter = "e"
        elif caracter == "į":
            caracter = "í"
        elif caracter == "ó":
            caracter = "o"
        elif caracter == "ú":
            caracter = "u"

                        
        if caracter not in repetidos and caracter.isalpha():
            distintos += 1
            repetidos.append(caracter)

    return distintos

if __name__ == "__main__":
    doctest.testmod()


