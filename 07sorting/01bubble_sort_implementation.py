def bubbleSort(array):
    length = len(array)
    for i in range(length-1):
        for j in range(length-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j] # Swap numbers

    return array

numbers = [99,44,6,2,1,5,63,87,283,4,0]
print(bubbleSort(numbers))




