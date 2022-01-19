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