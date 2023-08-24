def insertAtBeggining(self, data):
    newNode = Node()
    newNode.data = data
    if self.length == 0:
        self.head = newNode
    else:
        newNode.next = self.head
        self.head = newNode
    self.length += 1
    
