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


class LinkedList(object):

    def __init__(self):
        self.length = 0
        self.head = None

    def setHead(self, Node):
        self.head = Node

    def getHead(self):
        return self.head 

    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.data = data
        if self.length == 0:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def insertAtEnd(self, data):
        newNode = Node()
        newNode.data = data
        if ( self.length == 0 ):
          self.head = newNode
          self.length +=1
          return
        current = self.head
        while current.next != None:
          current = current.next
        current.next = newNode
        self.length +=1


    def insertAtGivenPosition(self, pos, data):
        if pos > self.length or pos < 0:
          return None
        else:
          if pos == 0:
            self.insertAtBeginning(data)
          else:
            if pos == self.length:
              self.insertAtEnd(data)
            else:
              newNode = Node()
              newNode.data = data
              count = 1
              current = self.head
              while count < pos-1:
                count +=1
                current = current.next
              newNode.next = current.next
              current.next = newNode
              self.length +=1


    def deleteFromBeginning(self):
        if self.length != 0:
          self.head = self.head.next
          self.length -=1


    def deleteFromEnd(self):
        if self.length != 0:
          currentNode = self.getHead()
          previousNode = self.getHead()
          while currentNode.next != None:
            previousNode = currentNode
            currentNode = currentNode.next
          previousNode.next = None
          self.length -=1


    def deleteAtPosition(self,pos):
        count = 0
        currentNode = self.head
        previousNode = self.head

        if pos > self.length or pos <0:
          return None
        else:
          while currentNode.next!=None or count <pos:
            count = count+1
            if count == pos:
              previousNode.next=currentNode.next
              self.length-=1
              return
            else:
              previousNode=currentNode
              currentNode=currentNode.next

    def printDLL(self):
          current = self.head
          while current != None:
              print(current)
              current = current.next  

    def encontrarNTermoAPartirDaCauda(self, n):
    # Step 1: Determine the length of the linked list
      current = self.head
      length = 0
      while current:
        length += 1
        current = current.next

    # Step 2: Traverse to the node at position M - n + 1
      position = length - n + 1
      if position <= 0:
        return None
    
      current = self.head
      for _ in range(position - 1):
          current = current.next
    
      return current



''' LL = LinkedList()



LL.insertAtBeginning(1)
LL.insertAtBeginning(5)
LL.insertAtBeginning(3)
LL.insertAtBeginning(9)



LL.printDLL() 

n = 2
enesimoTermo = LL.encontrarNTermoAPartirDaCauda(n)
if enesimoTermo:
    print(f"{n} termo a partir da cauda e:", enesimoTermo.data)
else:
    print(f"Nenhum {n} termo a partir da cauda encontrado.")


n = 4
enesimoTermo = LL.encontrarNTermoAPartirDaCauda(n)
if enesimoTermo:
    print(f"{n} termo a partir da cauda e:", enesimoTermo.data)
else:
    print(f"Nenhum {n} termo a partir da cauda encontrado.")

'''


# QUESTAO 14

def split_linked_list(linked_list):
    if linked_list.head is None:
        return None, None

    slow_ptr = linked_list.head
    fast_ptr = linked_list.head

    # Move o ponteiro rápido duas vezes mais rápido que o lento
    while fast_ptr.next != linked_list.head and fast_ptr.next.next != linked_list.head:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    # Se o número de elementos na lista for ímpar, avance o ponteiro rápido mais uma vez
    if fast_ptr.next.next == linked_list.head:
        fast_ptr = fast_ptr.next

    # Cria duas novas listas circulares
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()

    # Configura os ponteiros de término para ambas as novas listas
    linked_list1.head = linked_list.head
    linked_list2.head = slow_ptr.next

    # Encerra as novas listas configurando os últimos nós para apontar para o início
    current1 = linked_list1.head
    while current1.next != linked_list.head:
        current1 = current1.next
    current1.next = linked_list1.head

    current2 = linked_list2.head
    while current2.next != slow_ptr.next:
        current2 = current2.next
    current2.next = linked_list2.head

    return linked_list1, linked_list2

def display_linked_list(linked_list):
    if linked_list.head is None:
        return

    current = linked_list.head
    while True:
        print(current.data, end=" -> ")
        current = current.next
        if current == linked_list.head:
            break
    print(linked_list.head.data)


#questao 15

def interlace_linked_lists(L1, L2):
    if not L1.head:
        return L2
    if not L2.head:
        return L1

    current1 = L1.head
    current2 = L2.head

    while current1 and current2:
        next1 = current1.next
        next2 = current2.next

        current1.next = current2
        current2.next = next1

        current1 = next1
        current2 = next2

    return L1