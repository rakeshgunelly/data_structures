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

    # This is of O(1) time complexity as there are no loops
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

    # This is of O(1) time complexity as there are no loops
    def preappend(self,data):
        prepend_node = Node(data)

        prepend_node.next = self.head
        self.head = prepend_node

        self.length += 1

    # This is of O(m) time complexity as we are looping througth the linked list once in traverse_to_index method
    def insert(self,index,data):
        

        if index >= self.length:
            self.append(data)
            print("The index is higher than the length of the linked list, hence the node is appended to the linked list")
            return

        new_node = Node(data)
        leader = self.traverse_to_index(index-1)
        holding_pointer = leader.next
        leader.next = new_node
        new_node.next = holding_pointer
        self.length+=1

        self.print_linked_list()


    # This is of O(m) time complexity as we are looping througth the linked list once
    def traverse_to_index(self,index):
            
        counter = 0
        current_node = self.head

        while(counter!= index):
            current_node = current_node.next
            counter+=1

        return current_node

    # This is of O(m) time complexity as we are looping througth the linked list once in traverse_to_index method
    def delete(self,index):

        if 0 >= index >= self.length:
            print("Please enter an index with in the range of the length of the linked list")
            return

        leader = self.traverse_to_index(index-1)
        unwanted_node = self.traverse_to_index(index)
        leader.next = unwanted_node.next
        self.length -=1
        self.print_linked_list()

    # This is of O(m) time complexity as we are looping througth the linked list once 
    def print_linked_list(self):
        linked_list = []
        current_node = self.head

        while (current_node != None):
            linked_list.append(current_node.data)
            current_node = current_node.next
        
        print(linked_list)

    def reverse(self):
        pass



newlinkedList = LinkedList()
newlinkedList.append(12)
newlinkedList.append(15)
newlinkedList.append(22)
newlinkedList.append(33)
newlinkedList.append(44)
# newlinkedList.insert(2,99)
# newlinkedList.insert(3,88)
newlinkedList.print_linked_list()
newlinkedList.delete(2)