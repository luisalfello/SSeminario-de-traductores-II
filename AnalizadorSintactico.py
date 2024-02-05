from Pila import *

class AnalizadorSintactico:
    def __init__(self):
        self.pila = Pila()
        self.tablaLR = [[2, 0, 0, 1],
                        [0, 0,-1, 0],
                        [0, 3,-3, 0],
                        [2, 0, 0, 4],
                        [0, 0,-2, 0]]

    def Analisis(self,cadena):

        self.pila.push(Terminal('$'))
        self.pila.push(Estado(0))
        
        accion = 0
        cadena = cadena.split()
        cadena.append('$')

        iter = 0

        print(f'Cadena a analizar: {cadena}')

        while accion != -1:
            # Analizamos la accion que se realizara, 
            # segun los elemtos de la tabla
            fila = self.pila.top()                       # Ultimo elemento de la pila
            columna = SelectType(cadena[iter])           # Tipo de dato
            accion = self.tablaLR[fila][columna]         # Accion que se realizara
            self.pila.show()
            
            if accion > 0:
                # Desplaza si es positivo la accion
                self.pila.push(Terminal(cadena[iter]))
                self.pila.push(Estado(accion))
                iter += 1
            elif accion < 0:
                # Eliminamos elementos segun la regla en la que caimos para validar
                if accion == -1:
                    print(f'Elemento valido...') 
                    if regla == -2:
                        print(f'Regla aplicada: E-> id + E')
                    elif regla == -3:
                        print(f'Regla aplicada: e -> id')
                    break
                elif accion == -2:# Regla E -> id + id 
                    # Reduce
                    for i in range(6):
                        self.pila.pop()
                elif accion == -3: # Regla E -> id
                    self.pila.pop()
                    self.pila.pop()
                regla = accion
                fila = self.pila.top()
                columna = 3
                accion = self.tablaLR[fila][columna]

                # Agregamos nuevos elemtos a la pila para validar la regla
                self.pila.push(NoTerminal('E'))
                self.pila.push(Estado(accion))
            else: 
                print(f'Elemento invalido...')
                break
            self.pila.tipo()
        
    # agregar que regla fue la que cumplio los objetivos.
        

def SelectType(elem):
        if elem == '+':
            return 1
        elif elem == '$':
            return 2
        else:
            return 0