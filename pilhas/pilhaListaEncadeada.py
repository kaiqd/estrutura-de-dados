class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
       return "Node[Data=%s]" % self.data

    def setData(self, data):
        self.data = data
    
    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next
    
    def hasNext(self):
        return self.next != None

class Stack(object):
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            raise IndexError("A pilha está vazia.")
        temp = self.head.data
        self.head = self.head.next
        return temp
    
    def peak(self):
        if self.isEmpty():
            raise IndexError("A pilha está vazia.")
        return self.head.data

    def isEmpty(self):
        return self.head is None

    def print_stack(self):
        current = self.head
        print("Elementos da pilha:")
        while current:
            print(current.data)
            current = current.next
    
    def isEmpty(self):
        return self.head is None

    def print_stack(self):
        current = self.head
        print("Elementos da pilha:")
        while current:
            print(current.data)
            current = current.next

pilha = Stack()

pilha.push(40)
print(pilha.pop()) # remove e retorna 40
print(pilha.isEmpty()) # retorna True


# Crie um programa que verifique se os delimitadores de uma expressão matemática estão corretamente dispostos.

def verifica_delimitadores(expressao):
    stack = Stack()
    delimitadores_abertos = "([{"
    delimitadores_fechados = ")]}"

    for char in expressao:
        if char in delimitadores_abertos:
            stack.push(char)
        elif char in delimitadores_fechados:
            if stack.isEmpty():
                return False
            topo = stack.pop()
            if not delimitadores_compativeis(topo, char):
                return False

    return stack.isEmpty()

def delimitadores_compativeis(op, end):
    return (op == "(" and end == ")") or \
           (op == "[" and end == "]") or \
           (op == "{" and end == "}")

# Exemplo de uso
expressao1 = "({[1 + 2] * 3})"
expressao2 = "({[1 + 2] * 3)}"

print(verifica_delimitadores(expressao1))  # Deve retornar True
print(verifica_delimitadores(expressao2))  # Deve retornar False
