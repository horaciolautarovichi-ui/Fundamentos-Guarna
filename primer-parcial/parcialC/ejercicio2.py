
# ==========================================
# Ejercicio 2
# ==========================================

"""
2) Se tiene una lista de listas de enteros, que se asume como matriz. Escribir en Python:

a. Una función que reciba la lista como parámetro y devuelva True si la matriz es cuadrada (n x n),
False de lo contrario.

b. Una función que reciba la lista como parámetro y devuelva True si la matriz es simétrica: el
elemento i, j debe ser igual al j, i para todo elemento de la matiz (para este punto asumir que la
matriz es cuadrada).
"""

def cuadrada(M):
    filas = len(M)
    columnas = len(M[0])

    valido = False

    if filas == columnas:
        valido = True


    return valido


def simetrica(M):
    valido = True
    filas = len(M)
    columnas = len(M[0])
    i = 0
    j = 0

    #USO WHILE YA QUE EN EL MOMENTO QUE ME CUENTA QUE ES NO ES SIMETRICO CORTO EL BUCLE

    while i < filas and valido:
        j = 0
        while j < columnas and valido:
            if M[i][j] != M[j][i]:
                valido = False
            j += 1
        i += 1    


    return valido 

