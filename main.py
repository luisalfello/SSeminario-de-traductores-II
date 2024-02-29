import numpy as np
from AnalizadorLexico import * 
from Pila import *
from AnalizadorSintactico import *

def compilador(dt):
    nReglas = int(dt.readline())                        # Leemos el numero de reglas
    vectores = []                                       # Declaramos el vector de los vectores
    for i in range(nReglas):                            # El for para añadir los vectores, segun el numero de reglas
        datos = ''.join(dt.readline()).replace('\n','')
        datos = ''.join(datos).replace('\t',' ')
        vectores.append(datos)                  
    nFilas = dt.readline()                              # Tomanos el numero de filas y columnas de la tabla
    nFilas = nFilas.split()

    datos = ''.join(dt.readlines()).replace('\n',' ')  # Tomanos el resto de la matriz quitando saltos de linea y puntos y comas
    datos = ''.join(datos).replace('\t',' ')
    datos = datos.split()
    iter = 0
    temp = []
    tablaLR = []
    for i in range(int(nFilas[0])):
        for j in range(int(nFilas[1])):
            temp.append(int(datos[iter]))
            iter += 1
        tablaLR.append(temp)
        temp = []
    #datos = np.matrix(datos)                            # Lo transformamos en matriz
    #datos.resize(int(nFilas[0]),int(nFilas[1]))

    for i in range(len(vectores)):                       # Dividimos los vectores
        vectores[i] = vectores[i].split()
        vectores[i][0] = int(vectores[i][0])             # Transformamos a numero el primer y segundo elementos del vector
        vectores[i][1] = int(vectores[i][1])

    return nReglas, vectores, tablaLR

if __name__=='__main__':
    data = open('compilador.lr','r') 
    cadena = open('cadena.txt','r')

    str = cadena.readlines()
    str.append('$')

    nReglas, vectores, tablaLR = compilador(data)

    sintactico = AnalizadorSintactico(tablaLR,str,vectores)

    sintactico.Analisis()

    #print(sintactico.vectores)

