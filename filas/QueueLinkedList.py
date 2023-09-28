

class Node:
    def __init__ (self, data=None, next=None, prev=None):
        self.data=data
        self.next=next
        self.prev=prev
    #Add getters and setters
    def __str__(self):
        return "Node[Data=%s]" % self.data

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