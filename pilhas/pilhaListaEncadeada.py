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
        while current:
            print(current.data)
            current = current.next

    def print_stack(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

pilha = Stack()

pilha.push(40)
#print(pilha.pop()) # remove e retorna 40
#print(pilha.isEmpty()) # retorna True

def transferir_pilhas(S, T):
    while not S.isEmpty():
        T.push(S.pop())


pilha_S = Stack()
pilha_T = Stack()

# Adicionando alguns elementos à pilha S
pilha_S.push(1)
pilha_S.push(2)
pilha_S.push(3)
pilha_S.push(4)

print("Pilha S antes da transferencia: ")
pilha_S.print_stack()

# Transferindo os dados de S para T
transferir_pilhas(pilha_S, pilha_T)

print("\nPilha T apos a transferencia:")
pilha_T.print_stack()

def removerElementos(pilha):
    if pilha.peak is not None:
        pilha.pop()
        removerElementos(pilha)

def reverse(array):
    stack = Stack()
    array = []
    for element in array:
        stack.push(element)
    while not stack.isEmpty():
        array.append(stack.pop())
    return array

''' array = [4, 3, 2, 1]
arrayreverso = reverse(array)

print(array)
print(arrayreverso)

def push6(data):
    if a[0] == n-1:
        return None
    a[0] += 1
    a[a[0]] = data
    return None

def pop6():
    if a[0] == 0
        return None
    d = a[a[0]]
    a[0] -= 1
    return d

def peek6():
    a[0] = 0 '''



