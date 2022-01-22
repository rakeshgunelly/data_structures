class Stack():

    def __init__(self) -> None:
        self.stackList = []
        self.length = 0

    def peek(self):
        return self.stackList[self.length   -1]

    def push(self,value):
        self.stackList.append(value)
        self.length +=1
        return 

    def pop(self):
        popped_item = self.stackList[self.length-1]
        self.stackList.pop()
        self.length -=1
        return popped_item
        
    def printStack(self):

        for i in self.stackList:
            print(i, end = '-->')




myStack = Stack()
myStack.push('Google')
myStack.push('Facebook')
myStack.push('Microsoft')
print(myStack.pop())
myStack.printStack()