

def ingresar_lista():

    lista = []

    num = int(input("Ingresa valores a la lista (escribe 0 para terminar):"))

    while num != 0:
        lista.append(num)
        num = int(input("Ingresa valores a la lista (escribe 0 para terminar):"))

    print("mostrar lista")


def mostrar_lista(lista):
    for valores in lista:
        print(valores)


def num_pares(lista):
    pares = 0
    i = 0
    tercer_par = 0
    while pares < 3 and i < len(lista):
        if lista[i] % 2 == 0:
            pares = pares + 1
        i = i + 1    

    if pares == 3:
        tercer_par = lista[i-1]  
        print(f"el tercer numero par es {tercer_par}")
    else:
        print(lista)

def main():
    m1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    m2 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    resultante = []

    for i in range(0,len(m1)):
        for j in range(0, len(m1[0])):
            




main()