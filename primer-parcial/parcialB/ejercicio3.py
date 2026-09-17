# ==========================================
# Ejercicio 3
# ==========================================

"""
Dada una lista de listas llamada frase_morfologica, donde cada sublista contiene una palabra y su categoría morfológica, por
ejemplo:
    [["El", "art"], ["búho", "sust"], ["cantó", "verbo"], ["durante", "prep"], ["la", "art"], ["noche", "sust"], ["entera", "adj"]]

Se pide:

1. Generar un diccionario cuya clave sea el tipo morfológico y cuyo valor sea una lista con 4 enteros en este orden:
    - cantidad de palabras que empiezan y terminan en consonante
    - cantidad de palabras que empiezan en vocal y terminan en consonante
    - cantidad de palabras que empiezan en consonante y terminan en vocal
    - cantidad de palabras que empiezan en vocal y terminan en vocal

    Ejemplo: "art": [0, 1, 1, 0], "adj": [0, 0, 0, 1], etc.

2. Imprimir un listado con los tipos de palabras que empiezan y terminan en vocal, ordenado de mayor a menor cantidad,
con el formato:

    Tipo - cantidad
"""

def morfologica(frase_morfologica):

    diccionario = {}

    for frase in frase_morfologica:

        tipo =  frase[1]
        palabra = frase[0].lower()

        #si el tipo no esta en el diccionario lo creamos

        if tipo not in diccionario:
            diccionario[tipo] = [0, 0, 0, 0]
        
        if palabra[0].isalpha() and palabra[-1].isalpha() and palabra[0] not in "aeiouáéíóú" and palabra[-1] not in "aeiouáéíóú":
            diccionario[tipo][0] += 1
        elif palabra[0] in "aeiouáéíóú" and palabra[-1].isalpha() and palabra[-1] not in "aeiouáéíóú":
            diccionario[tipo][1] += 1
        elif palabra[0].isalpha() and palabra[0] not in "aeiouáéíóú" and palabra[-1] in "aeiouáéíóú":
            diccionario[tipo][2] += 1
        elif palabra[0] in "aeiouáéíóú" and palabra[-1] in "aeiouáéíóú":
            diccionario[tipo][3] += 1

    return diccionario

def mostrar_vocales(diccionario):
    listado = []

    for categoria in diccionario:
        cantidad = diccionario[categoria][3]
        if cantidad > 0:
            listado.append([cantidad],[categoria]) #primero cantidad para q se ordene numericamente


    #en este punto ya tenemos la lista cargada
    listado.sort(reverse=True) ##menor a mayor 

    print("tipo - cantidad")
    for lista in listado:
        print(f"{lista[1]} - {lista[0]}")

    
