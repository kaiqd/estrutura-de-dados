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