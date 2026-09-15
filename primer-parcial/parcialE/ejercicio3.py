# ==========================================
# Ejercicio 3
# ==========================================

"""
Se cuenta con una lista votacion, ya cargada, que contiene sublistas.
Cada una de esas sublistas tiene los siguientes valores: partido (string), nro. de mesa (entero), diputados (entero), senadores (entero)
Ejemplo: [["PP", 2, 19, 35], ["PSOE", 13, 20, 30], ["VOX", 2, 15, 15], ["PP", 5, 0, 15], ["VOX", 5, 10, 13], ["PP", 13, 9, 5], ...].
Los recuentos son de diferentes mesas por lo que los nombres de los partidos aparecerán varias veces.

Se pide que escribas un programa modular en Python (compuesto por funciones), que procese la lista votacion una única
vez y:
1. Obtenga la lista votación invocando a la función obtener_votos de la librería votacion2024.
2. Genere un diccionario con clave partido y valores total_diputados, total_senadores.
3. Imprima un listado de los partidos con el respectivo total de votos obtenidos (diputados + senadores) y el
porcentaje que representa el total de votos obtenidos sobre el total general, ordenados de mayor a menor por el
total de votos obtenidos. El listado debe tener un formato de 3 columnas.
Informe el total de mesas escrutadas.
"""