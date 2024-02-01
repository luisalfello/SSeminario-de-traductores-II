from Pila import *

def SelectType(elem):
    if elem == '+':
        return 1
    elif elem == '$':
        return 2
    else:
        return 0

if __name__=='__main__':
    Ejercicio1 = "hola +"
    Ejercicio2 = "a + b + c + d + e + f"
    cadena = Ejercicio1
    pila = Pila()
    #######################################
    tablaLR = [[2, 0, 0, 1],
               [0, 0,-1, 0],
               [0, 3,-3, 0],
               [2, 0, 0, 4],
               [0, 0,-2, 0]]

    pila.push('$')
    pila.push(0)
    
    accion = 0
    cadena = cadena.split()
    cadena.append('$')

    iter = 0

    print(f'Cadena a analizar: {cadena}')

    while accion != -1:
        # Analizamos la accion que se realizara, 
        # segun los elemtos de la tabla
        fila = pila.top()                       # Ultimo elemento de la pila
        columna = SelectType(cadena[iter])      # Tipo de dato
        accion = tablaLR[fila][columna]         # Accion que se realizara
        pila.show()
        
        if accion > 0:
            # Desplaza si es positivo la accion
            pila.push(cadena[iter])
            pila.push(accion)
            iter += 1
            #if iter > len(cadena)+8:break
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
                    pila.pop()
            elif accion == -3: # Regla E -> id
                pila.pop()
                pila.pop()
            regla = accion
            fila = pila.top()
            columna = 3
            accion = tablaLR[fila][columna]

            # Agregamos nuevos elemtos a la pila para validar la regla
            pila.push('E')
            pila.push(accion)
        else: 
            print(f'Elemento invalido...')
            break
    
# agregar que regla fue la que cumplio los objetivos.
    

