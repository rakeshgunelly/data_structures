# Linked list implementation in python 

# 12 --> 15 -- > 18

class Node():

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self,head):
        self.head = None
        self.tail = None