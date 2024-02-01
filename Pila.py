class Pila:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def show(self):
        for i in range(len(self.items)):
            print(self.items[i],end=" ")
        print('\n')

    def top(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)