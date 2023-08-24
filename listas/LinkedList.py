class LinkedList(object):

    def __init__(self):
        self.length = 0
        self.head = None


    def setHead(self, Node):
        self.head = Node

    def getHead(self):
        return self.head
