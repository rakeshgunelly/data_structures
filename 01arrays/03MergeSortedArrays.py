"""Problem : Given two sorted lists [0,3,4,31],[4,6,30]. Merge the two lists so that the 
final merged list is also sorted ie. O/P :[0,3,4,4,6,30,31]
"""

def sorted_arrays(array1,array2):
    mergedArray = []

    i = 0
    j = 0

    if len(array1)==0 or len(array2)==0:
        return array1+array2
    

    while(i < len(array1) & j < len(array2)):
        if ( array1[i]<array2[j] ):
            mergedArray.append(array1[i])
            i+=1
        else:
            mergedArray.append(array2[j])
            j+=1

    return mergedArray + array1[i:]+array2[j:]

print(sorted_arrays([0,3,4,31],[4,6,30]))
