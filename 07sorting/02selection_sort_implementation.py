def selectionSort(array):
    length = len(array)
    for i in range(length):
        min = i
        temp = array[i]
        for j in range(i+1,length):
            if(array[j]<array[min]):
                min = j

        array[i] = array[min]
        array[min] = temp

    return array

numbers = [99,44,6,2,1,5,63,87,283,4,0]
print(selectionSort(numbers))

