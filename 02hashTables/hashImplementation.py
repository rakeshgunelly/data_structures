#Hash map implementation in Python


class HashTable :
    
    def __init__(self,size) -> None:
        self.size = size
        self.data = [[] for i in range(size)]
        


    # Hash fucntion to generate a hash key, here the hash key is generated in a way that it will never exceed the size of array initialized
    def _hash(self, key):            
        hash = 0

        for i in range(0,len(key)-1):
            hash = (hash + ord(key[i])*i)%(len(self.data))   #ord() function return unicode of a given character
        
        return hash

    # returns the hash value using the private hash method
    def get_hash_value(self,key):
        return self._hash(key)
    
    # For creating a [key,value] pair
    def set(self,key,value):       
        
        hash = self.get_hash_value(key)
    
        if self.data[hash]==[]:
            self.data[hash]=[key,value]
        elif self.data[hash][0]==key:
            print("Given key is already present in the hashmap, please enter a different key")
  

    #For fetching the value based on the given key
    def get(self,key):
        hash = self.get_hash_value(key)
        print(hash)
        if self.data[hash][0]==key:
            return self.data[hash][1]

        return "Given Key has no corresponding value pair"

    
    # For removing a [key,value] pair in a hash map
    def remove(self,key):
        hash = self._hash(key)
        reference = self.data[hash]

        for i in range (len(reference)):
            if reference[i][0]==key:
                reference.pop(i)

some_hash = HashTable(50)
some_hash.set('grapes',10000)
some_hash.set('grape',10000)
some_hash.set('apples',222)
some_hash.set('mango',111)
print(some_hash.data)                           # not a good way to access class data, using here only for verification
print(some_hash.get('grapes'))
print(some_hash.get('grap'))
#some_hash.remove('mango')
#print(some_hash.data) 
