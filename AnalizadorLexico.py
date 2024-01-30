cadena = "id int 1y - ) \"cadena\" || 1+5 6 -3 + * / = < > >= { $ } <= && ! != == ; , ( return"
estado = 0
lista_estados = []
iter = 0
simbolo = ""
print (cadena,'\n-----------------------------------')

def validar(sim, edo):
    if edo == -1:
        print(sim, '\t\terror')
    elif edo == 1:
        print(sim, '\t\tid')
    elif edo == 2:
        print(sim, '\t\tNatural')
    elif edo == 4:
        print(sim, '\t\tEntero')
    elif edo == 7:
        print(sim, '\t\tCadena')
    elif edo == 8:
        print(sim, '\t\ttipo')
    elif edo == 9:
        print(sim, '\t\tOpSuma')
    elif edo == 10:
        print(sim, '\t\tOpMul')
    elif edo == 12:
        print(sim, '\t\tOpRel')
    elif edo == 14:
        print(sim, '\t\tOpOr')
    elif edo == 16:
        print(sim, '\t\tOpAnd')
    elif edo == 17:
        print(sim, '\t\tOpNot')
    elif edo == 18:
        print(sim, '\t\tIgual')
    elif edo == 19:
        print(sim, '\t\tOpIgualdad')
    elif edo == 20:
        print(sim, '\t\t;')
    elif edo == 21:
        print(sim, '\t\t,')
    elif edo == 22:
        print(sim, '\t\t(')
    elif edo == 23:
        print(sim, '\t\t)')
    elif edo == 24:
        print(sim, '\t\t{')
    elif edo == 25:
        print(sim, '\t\t}')
    elif edo == 26:
        print(sim, '\t\tif')
    elif edo == 27:
        print(sim, '\t\twhile')
    elif edo == 28:
        print(sim, '\t\treturn')
    elif edo == 29:
        print(sim, '\t\telse')
    elif edo == 30:
        print(sim, '\t\t$')
    

for i in cadena+' ':
    # Estado Inicial
    if estado == 0:
        try:
            simbolo = simbolo[:-1]
            validar(simbolo,lista_estados[-1])
        except IndexError:
            pass
        simbolo = ''
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            estado = 1
        elif (i >= '0' and i <= '9'):
            estado = 2
        elif (i == '-'):
            estado = 3
        elif (i == '\'' or i == '\"'):
            estado = 5
        elif(i == '+'):
            estado = 9
        elif(i == '*' or i == '/'):
            estado = 10
        elif(i == '<' or i == '>'):
            estado = 11
        elif(i == '|'):
            estado = 13
        elif(i == '&'):
            estado = 15
        elif(i == '!'):
            estado = 17
        elif(i == '='):
            estado = 18
        elif(i == ';'):
            estado = 20
        elif(i == ','):
            estado = 21
        elif(i == '('):
            estado = 22
        elif(i == ')'):
            estado = 23
        elif(i == '{'):
            estado = 24
        elif(i == '}'):
            estado = 25
        elif(i == '$'):
            estado = 30
        
        else:
            estado = -1
    
    # Estado de identificadores        
    elif estado == 1:
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            estado = 1
        elif i >= '0' and i <= '9':
            estado = 1
        elif i == ' ':
            if simbolo == 'int' or simbolo == 'float' or simbolo == 'void':
                estado = 8
                lista_estados.append(estado)
                estado = -2
            elif simbolo == 'if':
                estado = 26
                lista_estados.append(estado)
                estado = -2
            elif simbolo == 'while':
                estado = 27
                lista_estados.append(estado)
                estado = -2
            elif simbolo == 'return':
                estado = 28
                lista_estados.append(estado)
                estado = -2
            elif simbolo == 'else':
                estado = 29
                lista_estados.append(estado)
                estado = -2
            else:
                lista_estados.append(estado)
                estado = -2
        else:
            estado = -1
    
    # Estado de naturales
    elif estado == 2:
        if (i >= '0' and i <= '9') :
            estado = 2
        elif i == ' ':
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1
    
    # Estado de Enteros
    elif estado == 3:
        if (i >= '0' and i <= '9') :
            estado = 4
        elif i == ' ':
            estado = 9
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1
    
    elif estado == 4:
        if i >= '0' and i <= '9':
            estado = 4
        elif i == ' ':
            lista_estados.append(estado)
            estado = -2

    # Estado de cadena
    elif estado == 5:
        if i == '\'' or i == '\"':
            estado = 7
        else:
            estado = 6

    elif estado == 6:
        if i == '\'' or i == '\"':
            estado = 7
        else:
            estado = 6

    elif estado == 7:
        if i == ' ':
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1

    # Estado OpSuma
    elif estado == 9:
        if i == ' ':
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1

    # Estado OpMul
    elif estado == 10:
        if i == ' ':
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1

    # Estado de OpRel
    elif estado == 11:
        if i == '=':
            estado = 12
        elif i == ' ':
            estado = 12
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1        

    elif estado == 12:
        if i == ' ':
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1

    # Estado de OpOr
    elif estado == 13:
        if i == '|':
            estado = 14
        else:
            estado = -1
    elif estado == 14:
        if i == ' ':
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1

    # Estado de OpAnd
    elif estado == 15:
        if i == '&':
            estado = 16
        else:
            estado = -1
    elif estado == 16:
        if i == ' ':
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1
    
    # Estado de OpNot
    elif estado == 17:
        if i == ' ':
            lista_estados.append(17)
            estado = -2
        elif i == '=':
            estado = 19
        else:
            estado = -1

    # Estado de OpIgualdad
    elif estado == 18:
        if i == '=':
            estado = 19
        elif i == ' ':
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1
    elif estado == 19:
        if i == ' ':
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1

    # Estado de ;
    elif estado == 20:
        if i == ' ':
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1
    
    # Estado de ,
    elif estado == 21:
        if i == ' ':
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1

    #Estado de (
    elif estado == 22:
        if i == ' ':
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1

    #Estado de )
    elif estado == 23:
        if i == ' ':
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1

    #Estado de {
    elif estado == 24:
        if i == ' ':
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1

    #Estado de }
    elif estado == 25:
        if i == ' ':
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1

    #Estado de $
    elif estado == 30:
        if i == ' ':
            lista_estados.append(estado)
            estado = -2
        else:
            estado = -1

    # Estado de error
    if estado == -1:
        if i == ' ':
            lista_estados.append(estado)
            estado = 0
        else:
            estado = -1
    
    # Estado cuando se encuentra espacio en la cadena        
    if estado == -2:
        estado = 0
    
    simbolo = simbolo + i

lista_estados.append(estado)  
validar(simbolo, lista_estados[-2])
print(lista_estados)    

        