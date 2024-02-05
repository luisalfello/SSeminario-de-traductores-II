from Pila import *
from AnalizadorSintactico import *

if __name__=='__main__':
    Ejercicio1 = "hola + mundo"
    Ejercicio2 = "a + b + c + d + e + f"
    cadena = Ejercicio2
    
    analasis = AnalizadorSintactico()

    analasis.Analisis(cadena)
