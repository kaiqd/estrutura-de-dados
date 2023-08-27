class Node:
   def __init__ (self, data=None, next=None, prev=None):
       self.data=data
       self.next=next
       self.prev=prev
   #Add getters and setters
   def __str__(self):
       return "Node[Data=%s]" % self.data
  
class DoublyLL:
  
   def __init__(self):
       self.length= 0
       self.head= None
       self.tail= None


   def insertAtGivenPosition(self, pos, data):
       if self.head==None or pos ==0:
           self.insertAtBeginning(data)
       elif pos == self.length:
           self.insertAtEnd(data)
       elif pos < self.length:
           curr = self.head
           count = 0
           while curr != None and count < pos:
               curr = curr.next
               count +=1
           newNode = Node(data)
           newNode.next = curr.next
           newNode.prev = curr
           curr.next = newNode
           length += 1
  
   def insertAtBeginning(self, data):
       newNode = Node(data, None, None)
       if(self.head==None):
           self.head = self.tail = newNode
       else:
           newNode.prev=None
           newNode.next=self.head
           self.head.prev = newNode
           self.head = newNode
       self.length += 1


   def insertAtEnd(self,data):
       newNode = Node(data)
       if(self.length == 0):
           self.head =self.tail = newNode
       else:
           newNode.prev = self.tail
           self.tail.next = newNode
           self.tail = newNode
       self.length += 1

   def removeAtBeginning(self):
        if self.head is None:
            print("Lista vazia. Nada para remover.")
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1

   def removeAtEnd(self):
        if self.head is None:
            print("Lista vazia. Nada para remover.")
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1

   def removeAtPosition(self, pos):
        if pos < 0 or pos >= self.length:
            print("Posição inválida para remoção.")
            return
        if pos == 0:
            self.removeAtBeginning()
        elif pos == self.length - 1:
            self.removeAtEnd()
        else:
            curr = self.head
            count = 0
            while curr is not None and count < pos:
                curr = curr.next
                count += 1
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.length -= 1

   def printDLL(self):
        current = self.head
        while current != None:
            print(current)
            current = current.next


''' DLL = DoublyLL()

DLL.insertAtEnd(4)
DLL.removeAtBeginning()
DLL.insertAtBeginning(1)
DLL.insertAtBeginning(5)
DLL.insertAtBeginning(3)
DLL.insertAtBeginning(9)
DLL.removeAtEnd()

DLL.printDLL()  

A impressão será 

Node[Data=9]
Node[Data=3]
Node[Data=5] '''
