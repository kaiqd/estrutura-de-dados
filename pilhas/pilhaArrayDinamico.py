class Stack:
    def __init__(self, Capacity=1):
        self.top = -1
        self.Capacity = Capacity
        self.A = [None] * Capacity

    def push(self, data):
        if self.top == self.Capacity - 1:
            self.resize(1)
        self.top += 1
        self.A[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        if (self.top < self.Capacity //2):
            self.resize(0)
        temp = self.A[self.top]
        self.top -= 1
        return temp
    
    def resize(self, dir):
        if dir == 1:
            self.Capacity = self.Capacity*2
        else:
            self.Capacity = self.Capacity//2
        newArray = [None] * self.Capacity
        for i in range(0, self.top+1):
            newArray[i] = self.A[i]

        self.A = newArray

myStack = Stack(4)

myStack.push(30)

print(myStack.pop())