"""
Escribir una función que reciba el número de un mes, y devuelva el nombre del mes.
Por ejemplo, si la función recibe un "1", deberá devolver: "Enero"; si recibe un "2", deberá devolver: "Febrero"; y así con el resto de los valores.
En caso que el mes recibido no sea válido, deberá devolver "Mes Inválido".
No debe imprimir el nombre del mes, sólo devolver la cadena correspondiente.
Probá la función invoncándola desde el bloque principal, con al menos 3 valores.
"""


def num_mes(num):
    meses = ["enero", "febrero", "marzo","abril", "mayo" , "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    
    if num > 12 or num < 1:
        print("mes invalido")
    else:
        print(meses[num - 1])   
        


def main():
    num_mes((5))
    num_mes((8))
    num_mes((1))
    num_mes((-1))


main()
    