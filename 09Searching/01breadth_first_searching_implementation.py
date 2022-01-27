from fcntl import I_FLUSHBAND
from os import curdir
import queue


class Node():

    def __init__(self,value) -> None:
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree():

    def __init__(self) -> None:
        self.root = None


    def insert(self,value):
        newNode = Node(value)

        if (self.root == None):
            self.root = newNode
            return 
        else:
            currentNode = self.root
            while(True):
                if(value <currentNode.value):
                    # shift left
                    if (currentNode.left == None):
                        currentNode.left = newNode
                        return 
                    currentNode = currentNode.left
                else:
                    # shift right
                    if  (currentNode.right == None):
                        currentNode.right = newNode
                        return 
                    currentNode = currentNode.right

    def lookup(self,value):
        if self.root == None:
            return False
        else:
            currentNode = self.root

            while(currentNode):
                
                if currentNode.value> value:
                    # shift left 
                    currentNode = currentNode.left
                elif currentNode.value < value:
                    # shift right 
                    currentNode = currentNode.right
                else:
                    return True
                
        return False

    def remove(self,value):
        if self.root == None:
            return False
        currentNode = self.root
        parentNode = None
        while(currentNode):
            if(value<currentNode.value):
                parentNode = currentNode
                currentNode = currentNode.left
            elif(value>currentNode.value):
                parentNode = currentNode
                currentNode = currentNode.right
            elif (currentNode.value == value):
                if(currentNode.right == None):
                    if(parentNode == None):
                        self.root = currentNode.left
                    else:
                        pass
        
    
    def breadthFirstSearch(self):
        currentNode = self.root
        myList = []
        queue = []
        queue.append(currentNode)

        while len(queue)>0:

            currentNode = queue[0]
            del queue[0]
            myList.append(currentNode.value)

            if currentNode.left:
                myList.append(currentNode.left)
            if currentNode.right:
                myList.append(currentNode.right)

        return myList
        
    def recursiveBFS(self,queue,myList):
        if len(queue) == 0:
            return myList

        currentNode = queue[0]
        del queue[0]
        myList.append(currentNode.value)

        if currentNode.left:
            myList.append(currentNode.left)
        if currentNode.right:
            myList.append(currentNode.right)

        return self.recursiveBFS(queue,myList)

    def printTree(self):
        if self.root != None:
            self.treeTraversal(self.root)

    def treeTraversal(self,currentNode):
        if currentNode != None:
            self.treeTraversal(currentNode.left)
            print(str(currentNode.value))
            self.treeTraversal(currentNode.right)
            

#           9
#         /   \
#      4      20
#     /   \   /   \
#   1     6  15   170
tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree.lookup(10))
# tree.printTree()