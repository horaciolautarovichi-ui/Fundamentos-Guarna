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