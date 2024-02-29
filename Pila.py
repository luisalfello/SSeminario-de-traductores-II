

class ElementoPila:
    def __init__(self):
        self.simbolo = None
    
    def tipo():
        return False

class Estado(ElementoPila):
    def __init__(self, simbolo):
        self.simbolo = simbolo
        self.tipo = 'Estado'

class Terminal(ElementoPila):
    def __init__(self, simbolo):
        self.simbolo = simbolo
        self.tipo = 'Terminal'

class NoTerminal(ElementoPila):
    def __init__(self, simbolo):
        self.simbolo = simbolo
        self.tipo = 'noTerminal'

########################################################################
##############                    PILA                    ##############
########################################################################

class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def show(self):
        #print('\n')
        for obj in self.items:
            print(obj.simbolo ,end=" ")
        print('\n')
    
    def tipo(self):
        for i in range(1,3):
            print(f'Agregado: {self.items[-i].simbolo} de tipo: {self.items[-i].tipo}',end=" ")
        
    def top(self):
        return self.items[-1].simbolo
    