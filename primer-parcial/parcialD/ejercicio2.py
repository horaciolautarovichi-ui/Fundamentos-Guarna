# ==========================================
# Ejercicio 2
# ==========================================

"""
Escribí una función que devuelva verdadero si un alumno aprobó un curso virtual, o de lo contrario falso.
La función recibe dos listas: una de puntajes máximos por cada actividad y otra de puntajes otorgados por dicha
actividad.
Para aprobar el curso se necesita que en cada actividad haya obtenido, por lo menos, un 60% del puntaje máximo.
Evitar ciclos y evaluaciones innecesarias.
Además, agregá DOS casos de prueba adicionales, en donde uno sea Falso y el otro Verdadero, uno para listas de 5
puntajes, y otro para listas de 6 puntajes.

Casos de Prueba:
>>> aprobo_cursada([10, 20, 15], [6, 15, 12])
True
>>> aprobo_cursada([10, 20, 15], [6, 8, 12])
False
>>> aprobo_cursada([10, 20, 15, 30], [6, 12, 9, 12])
False
"""


