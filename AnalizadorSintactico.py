from Pila import *
from AnalizadorLexico import *

class AnalizadorSintactico:
    def __init__(self,tablaLR,str,vectores):
        self.pila = Pila()
        self.tablaLR = tablaLR
        lexico = analizadorLexico()
        self.cadena = lexico.separador(str)
        self.tipo = lexico.Analisis(self.cadena)
        self.vectores = vectores
        

    def Analisis(self):

        self.pila.push(Terminal('$'))
        self.pila.push(Estado(0))

        accion = 0


        print(f'Cadena a analizar: ')
        """for i in self.cadena:
            print(' '.join(i))"""
        
        simbolo = 0
        contador = 1
        j = 0
        while j < len(self.cadena):
            i = 0
            while i < len(self.cadena[j]):
                # Analizamos la accion que se realizara, 
                # segun los elemtos de la tabla
                fila = self.pila.top()                       # Ultimo elemento de la pila
                columna = self.tipo[simbolo]                 # Tipo de dato
                accion = self.tablaLR[fila][columna]         # Accion que se realizara
                print(f'Iteracion: {contador}')
                #print(f'>>>>accion: {accion}, item: {self.cadena[j][i]}')
                self.pila.show()

                if accion > 0:
                    # Desplaza si es positivo la accion
                    self.pila.push(Terminal(self.cadena[j][i]))
                    self.pila.push(Estado(accion))
                    simbolo += 1
                    i += 1
                elif accion < 0:
                    if accion == -1:
                        print('cadena valida...')
                        break
                    # Eliminamos elementos segun la regla en la que caimos para validar
                    regla = abs(accion)-1
                    #print(f'regla: {regla} pop: {self.vectores[regla-1][1]}')
                    for pop in range(self.vectores[regla-1][1]*2):
                        self.pila.pop()
                    fila = self.pila.top()
                    columna = self.vectores[regla-1][0]
                    accion = self.tablaLR[fila][columna]

                    # Agregamos nuevos elemtos a la pila para validar la regla
                    self.pila.push(NoTerminal(self.vectores[regla-1][2]))
                    self.pila.push(Estado(accion))
                else: 
                    print(f'Elemento invalido...')
                    break
                #self.pila.tipo()
                contador += 1
                print('===========================================')
            j += 1
    # agregar que regla fue la que cumplio los objetivos.
        