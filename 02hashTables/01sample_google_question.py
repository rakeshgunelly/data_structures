# Google Question 
# Given am array = [2,5,1,2,3,5,1,2,4]:
# return the first reccuring item i.e 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# it should return 1

# Given an array = [2,3,4,5]
# it should return undefined

# A brute force approch is to loop througth the given array and see if the given item is present in the array
# it will be of O(n^2) time complexity

# Brute force approach | Time complexity is O(n^2)

def first_reccurring_item(input):

    for i in range(len(input)-1):
        for j in range(i+1,len(input)-1):
            if input[i]==input[j]:
                return input[i]
    
    return False




# Using hashmaps: Here time complexity is O(n) as we are looping thrigth the elements once

def first_reccurring_item2(input):
    mydict = {}
    for i in range(len(input)):
        if input[i] in mydict:
            return input[i]
        else:
            mydict[input[i]]=i

    return 'No Reccuring values are present'



print(first_reccurring_item2([2,3,4,5]))