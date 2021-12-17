class MyArrays:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):              # this method is to print the output values in string format
        return str(self.__dict__)

    def get(self,index):            # this method is for accessing elements in the given index
        return self.data[index]     # this is of O(1), linear time complexity. 

    def push(self,item):            # this method is to push new elements into the array
        self.data[self.length]=item # this is of O(1), linear time complesity
        self.length+=1

    def pop(self):                  # this method is to pop the last element in the array
        last_item = self.data[self.length-1]
        del self.data[self.length-1]    # this is of O(1), linear time complesity
        self.length-=1
        return last_item

    def delete(self,index):         # this method deletes the element in the given index
        deleted_item = self.data[index]
        for i in range(index,self.length-1): # This is of O(n) time complexity as we are looping through 
            self.data[i]=self.data[i+1]      #  n(size of the array) elements 

        del self.data[self.length-1]
        self.length-=1
        return deleted_item

    def insert(self,index,item):     # this method inserts the given 'item' in the 'index' position mentioned
        self.length +=1
        for i in range(self.length-1,index,-1): 
            self.data[i]=self.data[i-1]     # This is of O(n) time complexity as we are looping through 
        self.data[index]=item               #  n(size of the array) elements 


newArray = MyArrays()   # creating an object of MyArrays Class
newArray.push(6)        # pushing elements into the array
newArray.push(7)
newArray.push(8)
newArray.push(9)
newArray.push(1)
newArray.push(2)
print(newArray.get(3)) # displaying element at index 3

print(newArray.pop())   # removing the last element 
newArray.insert(3,'a')  # adding 'a' at index 3 
newArray.delete(2)      # deleting element at index 2 
print(newArray)         # displaying the final array elements

