# Linked list implementation in python 

# 12 --> 15 -- > 18

class Node():

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
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
        prepend_node = Node(data)

        prepend_node.next = self.head
        self.head = prepend_node

        self.length += 1

        
    def insert(self,index,value):
        pass

    def delete(self,data):
        pass

    def print_linked_list(self):
        linked_list = []
        current_node = self.head

        while (self.head != None):
            linked_list.append(current_node.data)
            current_node = current_node.next
        
        print(linked_list)

    def reverse(self):
        pass



newlinkedList = LinkedList()
newlinkedList.append(10)
newlinkedList.append(5)
newlinkedList.append(6)