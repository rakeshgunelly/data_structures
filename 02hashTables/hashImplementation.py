#Hash map implementation in Python

class HashTable :
    
    def __init__(self,size) -> None:
        self.data = [[] for i in range(size)]
        


    # Hash fucntion to generate a hash key, here the hash key is generated in a way that it will never exceed the size of array initialized
    def _hash(self, key):            
        hash = 0

        for i in range(0,len(key)-1):
            print(ord(key[i]))
            hash = (hash + ord(key[i])*i)%(len(self.data))   #ord() function return unicode of a given character
        print("\n"+str(hash))
        return hash


    # For creating a [key,value] pair
    def set(self,key,value):       
        pass
        # address = self._hash(key)
        # if self.data[address] !=[]:
        #     self.data.insert(address,[key,value])
        
    #For fetching the value based on the given key
    def get(self,key):
        hash = self._hash(key)
        
        #for i in range(len(self.data[hash])):
        #    if self.data[i][0] == key:
        #        return self.data[i][1]

        reference = self.data[hash][0]
        print(reference)
    
        #for i in range(len(self.data)):
        #    if reference[i][0]==key:
        #        return reference[i][1]
            
        #return "Given Key has no corresponding value pair"

    
    # For removing a [key,value] pair in a hash map
    def remove(self,key):
        hash = self._hash(key)
        reference = self.data[hash]

        for i in range (len(reference)):
            if reference[i][0]==key:
                reference.pop(i)

some_hash = HashTable(50)
some_hash.set('grapes',10000)
# some_hash.set('grapes',10000)
# some_hash.set('grapes',10000)
some_hash.set('grapes',10000)
#some_hash.set('apples',222)
#some_hash.set('mango',111)
print(some_hash.data)                           # not a good way to access class data, using here only for verification
#print(some_hash.get('grapes'))
#print(some_hash.get('grap'))
#some_hash.remove('mango')
#print(some_hash.data) 
