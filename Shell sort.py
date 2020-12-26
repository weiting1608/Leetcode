def shell_sort(arr):
    sublistCount = len(arr)//2

    while sublistCount > 0:
        for start in range(sublistCount):

            gap_insertion_sort(arr,start,sublistCount)

        sublistCount = sublistCount//2
    return arr

def gap_insertion_sort(arr,start,gap):
    for i in range(start+gap,len(arr),gap):
        currentValue = arr[i]
        position = i

        while position >= gap and arr[position-gap] > currentValue:
            arr[position] = arr[position-gap]
            position = position-gap
        
        arr[position] = currentValue

arr = [45,6,7,23,564,32,80]
print(shell_sort(arr))    