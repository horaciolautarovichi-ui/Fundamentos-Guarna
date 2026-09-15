# ==========================================
# Ejercicio 1
# ==========================================

"""
Escribir una función que reciba una cadena de caracteres y devuelva una tupla con la cantidad de letras
mayúsculas, la cantidad de letras minúsculas y la cantidad de otros caracteres.
-> La primera posición en la tupla, corresponde a las letras mayúsculas; la segunda posición, a la
cantidad de letras minúsculas y la tercera a la cantidad de otros caracteres.
-> Las vocales acentuadas deben ser consideradas en los grupos de las letras.
-> Los espacios en blancos no deben ser contabilizados.
-> No se puede utilizar para esta solución el método count.

Ejemplo de casos y sus resultados:
Para ("Hola, ¿qué tal?") debe devolver (1, 9, 3)
Para ("HoLaChAu") debe devolver (4, 4, 0)
Para ("") debe devolver (0, 0, 0)
Para ("42910%(@!") debe devolver (0, 0, 9)
Para ("429A10É%(@!") debe devolver (2, 0, 9)
Para ("90em28ú") debe devolver (0, 3, 4)
Para ("A MÍ MI MAMÁ ME MIMA") debe devolver (15, 0, 0)
"""


