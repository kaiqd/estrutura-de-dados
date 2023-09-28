class Node:
    def __init__ (self, data=None, next=None, prev=None):
        self.data=data
        self.next=next
        self.prev=prev
    #Add getters and setters
    def __str__(self):
        return "Node[Data=%s]" % self.data

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
        while current:
            print(current.data)
            current = current.next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self, data):
        if ( self.size == 0):
            n = Node(data)
            self.front = n
            self.rear = n
            self.size += 1
        else:
            n = Node(data)
            
            if self.size == 1:
                self.front.next = n
                n.prev = self.front
            else:
                self.rear.next = n
                n.prev = self.rear
            self.rear = n
            self.size +=1
    
    def deQueue(self):
        if self.size == 0:
            raise IndexError
        else:
            n = self.front.data
            self.front = self.front.next
            self.size -= 1
            return n

    def front(self):
        return self.front.data

    def rear(self):
        return self.rear.data

    def isEmpty(self):
        return self.size == 0
    
    def print_queue(self):
        if self.size == 0:
            print("A fila está vazia.")
        else:
            current = self.front
            while current:
                print(current.data, end=" ")
                current = current.next
            print()
    
def inverter_fila_com_pilha(fila):
    pilha = Stack()

    # Enquanto a fila não estiver vazia, remova elementos da fila e empilhe-os na pilha
    while not fila.isEmpty():
        pilha.push(fila.deQueue())

    # Desempilhe os elementos da pilha e enfileire-os novamente
    while not pilha.isEmpty():
        fila.enQueue(pilha.pop())

    # Exemplo de uso
fila = Queue()
for i in range(1, 6):
    fila.enQueue(i)

print("Fila original:")
fila.print_queue()

inverter_fila_com_pilha(fila)

print("\nFila invertida:")
fila.print_queue()  



def inverter_pilha_com_fila(pilha):
    fila = Queue()

    # Enquanto a pilha não estiver vazia, remova elementos da pilha e enfileire-os na fila
    while not pilha.isEmpty():
        fila.enQueue(pilha.pop())

    # Desenfileire os elementos da fila e empilhe-os novamente na pilha
    while not fila.isEmpty():
        pilha.push(fila.deQueue())

# Exemplo de uso
pilha = Stack()
for i in range(1, 6):
    pilha.push(i)

print("\nPilha original: ")
pilha.print_stack()

inverter_pilha_com_fila(pilha)

print("\nPilha invertida: ")
pilha.print_stack()



def inverter_primeiros_k_elementos(fila, k):
    if k <= 0 or fila.isEmpty():
        return

    pilha = Stack()

    # Enfileira os primeiros k elementos em uma pilha
    for _ in range(min(k, fila.size)):
        pilha.push(fila.deQueue())

    # Desempilha os elementos da pilha e enfileira-os novamente na fila
    while not pilha.isEmpty():
        fila.enQueue(pilha.pop())

    # Move os elementos restantes para a fila
    for _ in range(fila.size - k):
        fila.enQueue(fila.deQueue())

# Exemplo de uso
fila = Queue()
for i in range(11, 21):
    fila.enQueue(i)

print("Fila original:")
fila.print_queue()

k = 3
inverter_primeiros_k_elementos(fila, k)

print(f"\nFila com os primeiros {k} elementos invertidos:")
fila.print_queue()



class FilaComDuasPilhas:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enQueue(self, data):
        # Empilhar o elemento na pilha 1
        self.stack1.push(data)

    def deQueue(self):
        # Se a pilha 2 estiver vazia, transferir elementos da pilha 1 para a pilha 2
        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())

        # Se ambas as pilhas estiverem vazias, gera erro
        if self.stack2.isEmpty() and self.stack1.isEmpty():
            raise IndexError("A fila está vazia.")

        # Pop da pilha 2 e retorna o elemento
        return self.stack2.pop()

# Exemplo de uso
fila = FilaComDuasPilhas()
fila.enQueue(1)
fila.enQueue(2)
fila.enQueue(3)

print("Fila original:")
try:
    print(fila.deQueue())
    print(fila.deQueue())
    print(fila.deQueue())
    print(fila.deQueue())  # Deve gerar um erro porque a fila está vazia
except IndexError as e:
    print(e)

    

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def addFront(self, data):
        new_node = Node(data, next=self.front)
        if self.isEmpty():
            self.rear = new_node
        else:
            self.front.prev = new_node
        self.front = new_node

    def addRear(self, data):
        new_node = Node(data, prev=self.rear)
        if self.isEmpty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

    def removeFront(self):
        if self.isEmpty():
            raise IndexError("DEQUE is empty.")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        return data

    def removeRear(self):
        if self.isEmpty():
            raise IndexError("DEQUE is empty.")
        data = self.rear.data
        self.rear = self.rear.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        return data

    def isEmpty(self):
        return self.front is None

    def printDeque(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage
deque = Deque()

deque.addRear(1)
deque.addRear(2)
deque.addFront(3)
deque.addFront(4)

print("Deque:")
deque.printDeque()

print("Removing from the front:", deque.removeFront())
print("Removing from the rear:", deque.removeRear())

print("Deque after removals:")
deque.printDeque()