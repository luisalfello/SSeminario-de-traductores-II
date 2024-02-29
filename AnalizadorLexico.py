class analizadorLexico():
    def __init__(self):
        pass

    def separador(self,str):
        for i in range(len(str)):
            str[i] = ''.join(str[i]).replace('\n','')

        aux = ''
        iter = 0
        for j in str:
            aux = ''
            for i in j:
                if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z'):
                    pass
                elif i == ' ':
                    pass
                elif i >= '0' and i <= '9':
                    pass
                elif i == '\"':
                    pass
                elif i == '.':
                    pass
                else:
                    j=''.join(j).replace(i,f' {i} ')
                aux = aux + i
            str[iter] = j.split()
            iter += 1
            
    
        return str

    def Analisis(self,cad):
        tipo = []
        tipos = []
        iteri = 0
        for i in cad:
            iterj = 0
            for j in i:
                if j[0] >= '0' and j[0] <= '9':
                    temp = float(j)
                    if(temp - int(temp) == 0):
                        tipo.append(1)
                    else:
                        tipo.append(2)
                elif j == 'int' or j == 'float' or j == 'void':
                    tipo.append(4)
                elif j == '+' or j == '-':
                    tipo.append(5)
                elif j == '*' or j == '/':
                    tipo.append(6)
                elif j == '<' or j == '>' or j == '<=' or j == '>=':
                    tipo.append(7)
                elif j == '||':
                    tipo.append(8)
                elif j == '&&':
                    tipo.append(9)
                elif j == '!':
                    tipo.append(10)
                elif j == '==' or j == '!=':
                    tipo.append(11)
                elif j == ';':
                    tipo.append(12)
                elif j == ',':
                    tipo.append(13)
                elif j == '(':
                    tipo.append(14)
                elif j == ')':
                    tipo.append(15)
                elif j == '{':
                    tipo.append(16)
                elif j == '}':
                    tipo.append(17)
                elif j == '=':
                    tipo.append(18)
                elif j == 'if':
                    tipo.append(19)
                elif j == 'while':
                    tipo.append(20)
                elif j == 'return':
                    tipo.append(21)
                elif j == 'else':
                    tipo.append(22)
                elif j == '$':
                    tipo.append(23)
                else:
                    tipo.append(0)
                tipos.append(list(tipo))
                iterj += 1
            iteri += 1
        return tipo