def insertion_sort(arr):
    # for every index in array
    for i in range(1, len(arr)):
        # set current values and position
        currentValue = arr[i]
        position = i
        
        #sorted sublist
        while position > 0 and arr[position-1] > currentValue:
            arr[position] = arr[position-1]
            position -= 1
    
        arr[position] = currentValue
    return arr

arr = [8,23,2,784,1,5] 
print(insertion_sort(arr))