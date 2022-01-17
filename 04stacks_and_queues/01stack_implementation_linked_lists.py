class Node():

    def __init__(self,data):
        self.data = data
        self.next = None

class Stack():

    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.data

    def push(self,value):
        newNode = Node(value)

        if(self.length == 0):
            self.top = newNode
            self.bottom = newNode
        else:
            holdingPOinter = self.top
            self.top = newNode
            self.top.next = holdingPOinter

        self.length += 1
        return self

    def pop(self):
        if(self.top == None):
            return None

        self.top = self.top.next
        self.length -= 1
        



myStack = Stack()
myStack.push('Google')
myStack.push('Facebook')
myStack.push('Microsoft')
print(myStack.peek())