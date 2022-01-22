# Queues can be implemented using boths lists(arrays) and linked lists. 
# But with lists(Arrays) the Dequeue operations would be mush costiler on time with time complexity as O(n) as we hav to shift the indexes
# So its is always better to implement with linked lists 


from time import sleep


class Node():

    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class Queue():

    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def peek(self): 
        if self.first!= None:
            print(self.first.value)
        else:
            print('Queue is empty')

    def dequeue(self):
        if(self.length ==0):
            print('Queue is empty')
        
        if(self.length == 1):
            self.last = None
        
        self.first = self.first.next
        self.length -= 1

        return


    def enqueue(self,value):
        newNode = Node(value)

        if (self.length == 0):
            self.first = newNode
            self.last = newNode
            self.length = 1
        else:
            self.last.next = newNode
            self.last = newNode
            self.length += 1

    def printQueue(self):
        temp = self.first
        while temp != None:
            print(temp.value , end = '-|-')
            temp = temp.next
        print()
        print(self.length)


myQueue = Queue()
myQueue.enqueue('Google')
myQueue.enqueue('facebook')
myQueue.enqueue('microsoft')
myQueue.printQueue()
myQueue.peek()
myQueue.dequeue()
myQueue.printQueue()
myQueue.dequeue()
myQueue.printQueue()