class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

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
    

def insertAtBeggining(self, data):
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