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

    def append(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def preappend(self,data):
        pass

    def insert(self,data):
        pass

    def delete(self,data):
        pass

    def print_linked_list(self,data):
        pass

    def reverse(self):
        pass