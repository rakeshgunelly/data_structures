def reverse_a_string(someString):
    reversedString = ''                     #an empty string to store the final output
    givenData =str(someString)              #converting input into string so that any data type 
                                            #can be converted into string
    if( len(givenData)<2 ):                 #if only one character is given as input we return the same 
        return givenData
    
    for i in range(len(givenData)-1,-1,-1): #looping in the reverse order and apending to an empty string
        reversedString += givenData[i]
        i-=1
    
    return reversedString           


print(reverse_a_string(12345))              #calling the function and printing the output 


#python inbuilt method for reversing a string is below
string1 = reversed('this is a string reversed using inbuilt method')

print(''.join(string1))


#let's try another approach using lists:
def another_approach(someString):
    return ''.join((list(str(someString))[::-1]))
    


print(another_approach(123456))

