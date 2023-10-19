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

fila = Queue()

fila.enQueue(1)
fila.enQueue(2)
fila.enQueue(3)
fila.deQueue()
fila.print_queue()