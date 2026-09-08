import doctest

def evaluar_perfecto(n):

    """
    >>> evaluar_perfecto(114574)
    False
    >>> evaluar_perfecto(47085659)
    False
    >>> evaluar_perfecto(20)
    False
    >>> evaluar_perfecto(28)
    True
    """

    perfecto = False #lo inicializamos en false ya que si no entra al if no es perfectoi 

    suma_divisores = 0
    i = 1
    if n >= 1:
    
        while i < n and suma_divisores < n :
            # Continuamos mientras no hayamos llegado al final de los posibles divisores
            # y mientras la suma de los divisores todavía sea menor que n
            if n % i == 0:
                suma_divisores += i
            i = i + 1
        if suma_divisores == n:
            perfecto = True
        
    return perfecto     


def main():
    print(doctest.testmod())

main()
