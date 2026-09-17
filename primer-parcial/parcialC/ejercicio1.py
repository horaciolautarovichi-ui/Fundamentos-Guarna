# ==========================================
# Ejercicio 1
# ==========================================

"""
1) Escribir una función validar que reciba una cadena de caracteres y devuelva True si una clave contiene las
restricciones requeridas, False de lo contrario.
- Debe contener entre 8 y 12 caracteres
- Debe contener por lo menos un carácter alfabético en mayúsculas (sin acentuar)
- Debe contener por lo menos tres caracteres alfabéticos en minúsculas (sin acentuar)
- Debe contener por lo menos dos dígitos numéricos
- Debe contener por lo menos alguno de los siguientes símbolos: [*, -, $, @]
- Cualquier otro símbolo que no esté en el grupo indicado rechazará la validación
"""

def validar (cadena):
    valido = False

    caracteres = len(cadena)
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minuscula = "abcdefghijklmnopqrstuvwxyz"
    simbolos = "*-$@"
    digitos = "1234567890"

    contador_minuscula = 0
    contador_digitos = 0
    contador_mayusculas = 0 
    contador_simbolos = 0

    i = 0
    if  8 <= caracteres <= 12:
        valido = True
        while i < caracteres and valido:
            if cadena[i] in minuscula:
                contador_minuscula += 1
            elif cadena[i] in mayusculas:
                contador_mayusculas += 1                    
            elif cadena[i] in digitos:
                contador_digitos += 1
            elif cadena[i] in simbolos:
                contador_simbolos += 1
            else:
                valido = False
            i += 1

    if valido:
        if contador_minuscula >= 3 and contador_mayusculas >= 1 and contador_simbolos > 0 and contador_digitos > 1:
            valido = True


    return valido
