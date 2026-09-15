# ==========================================
# Ejercicio 2
# ==========================================

"""
Escribí una función que reciba 3 listas que tendrán mediciones diarias de valores para distintas personas.
La primera lista es de temperaturas corporales, la segunda lista es de presencia de tos seca, y la tercera
es del nivel de cansancio (medido del 1 al 10).
La función tiene que devolver una lista con los índices (posiciones), que son sospechosos de COVID-19
con temperatura mayor o igual a 37 grados, presencia de tos y nivel de cansancio mayor a 6.

Ejemplos de Casos:
prueba_covid([35.6, 36.4, 35.2, 37.1], [True, False, True, True], [7, 2, 6, 8]) devuelve [3]
prueba_covid([38], [False], [9]) devuelve []
prueba_covid([40.2, 35.7, 38.4, 37.0], [True, False, True, True], [10, 2, 7, 8]) devuelve [0, 2, 3]

Invocá a la función con DOS casos de prueba distintos a los anteriores, en donde uno devuelva que el
paciente es sospechoso y otro en el que no.
"""


