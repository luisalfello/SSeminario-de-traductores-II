cadena = "cadena1 Prueba001  1variable 12 1y 1+5 "
estado = 0
i = 0
simbolo = ""
print (cadena,'\n-----------------------------------')

def validar(sim, edo):
    #print(edo)
    if edo == 3:
        print(sim, '\t\terror')
    elif edo == 1:
        print(sim, '\t\tid')
    elif edo == 2:
        print(sim, '\t\tEntero')
    


for i in cadena:
    # Estado Inicial
    if estado == 0:
        simbolo = ''
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            estado = 1
        elif i >= '0' and i <= '9':
            estado = 2
        else:
            estado = 3
    
    # Estado de identificadores        
    if estado == 1:
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            estado = 1
        elif i >= '0' and i <= '9':
            estado = 1
        elif i == ' ':
            validar(simbolo,estado)
            estado = 5
        else:
            estado = 3
    
    # Estado de enteros
    if estado == 2:
        if i >= '0' and i <= '9':
            estado = 2
        elif i == ' ':
            validar(simbolo,estado)
            estado = 5
        else:
            estado = 3
    
    # Estado de error
    if estado == 3:
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            estado = 3
        elif i >= '0' and i <= '9':
            estado = 3
        elif i == ' ':
            validar(simbolo,estado)
            estado = 0
        else:
            estado = 3
    
    # Estado cuando se encuentra espacio en la cadena        
    if estado == 5:
        estado = 0
    
    simbolo = simbolo + i
    #print(i,estado)
    
    
validar(simbolo, estado)

        