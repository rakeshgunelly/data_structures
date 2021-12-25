# Doubly Linked list implementation in python 

# 12 --> 15 -- > 18

class Node():

    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList():
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
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    # This is of O(1) time complexity as there are no loops
    def preappend(self,data):
        prepend_node = Node(data)

        prepend_node.next = self.head
        self.head.previous = prepend_node
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
        follower = self.traverse_to_index(index)
        leader.next = new_node
        new_node.previous = leader
        new_node.next = follower
        follower.next = new_node
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
    #TODO:  
    def delete(self,index):

        pass

    # This is of O(m) time complexity as we are looping througth the linked list once 
    def print_linked_list(self):
        linked_list = []
        current_node = self.head

        while (current_node != None):
            linked_list.append(current_node.data)
            current_node = current_node.next
        
        print(linked_list)

    # This is of O(m) time complexity as we are looping througth the linked list once 
    #TODO:  
    def reverse(self):
        pass



newlinkedList = DoublyLinkedList()
newlinkedList.append(12)
newlinkedList.append(15)
newlinkedList.preappend(22)
# newlinkedList.append(33)
# newlinkedList.append(44)
newlinkedList.insert(2,99)
# newlinkedList.insert(3,88)
newlinkedList.print_linked_list()
# newlinkedList.delete(2)