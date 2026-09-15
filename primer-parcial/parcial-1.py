##1- Escribir en Python una función que reciba una matriz (lista de listas) de enteros y devuelva True si esa matriz es cuadrada (las filas y las columnas tienen que ser ##de la misma longitud), False de lo contrario.

##2-Escribir en Python una función que reciba una matriz cuadrada (lista de listas) de enteros y devuelva True si esa matriz es diagonal superior (los elementos que están ##debajo de la diagonal principal, la que va de 1,1 a n,n, deben ser False de lo contrario.
                                                                                                                                                 
##3-Escribir en Python una función que reciba una matriz cuadrada (lista de listas) de enteros y devuelva True si esa matriz es la identidad, (los de la diagonal ##principal, la que va de 1,1 a n,n, deben ser 1 y todos los demás, 0, False de lo contrario.
                                                                                                                                             
##4-Escribir en Python una función que reciba una matriz (lista de listas) de enteros y devuelva una lista en donde el elemento i sea la suma de la fila i de la matriz.
##5-Escribir en Python una función que reciba una matriz (lista de listas) de enteros y devuelva una lista en donde el elemento i sea la suma de la columna i de la matriz.

def ejercicio1(M):
   filas = len(M)
   columnas = len(M[0])

   cuadrada = False

   if filas == columnas:
      cuadrada = True
      
   return cuadrada


    


     