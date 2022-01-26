

def mergesort(arrayList):
  if len(arrayList) == 1:
    return arrayList
  length = len(arrayList)
  mid = length // 2
  left = arrayList[:mid]
  right = arrayList[mid:]
  print('Left {}'.format(left))
  print('Right {}'.format(right))

  return merge(mergesort(left),mergesort(right))

def merge(left,right):
  result = []
  leftindex = 0
  rightindex = 0
  while leftindex < len(left) and rightindex < len(right):
    if left[leftindex] < right[rightindex]:
      result.append(left[leftindex])
      leftindex += 1
    else:
      result.append(right[rightindex])
      rightindex += 1
  print(left,right)
  print( result + left[leftindex:] + right[rightindex:] )
  return result + left[leftindex:] + right[rightindex:]

arrayList = [99,44,6,2,1,5,63,87,283,4,0]
print(mergesort(arrayList))
