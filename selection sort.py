def selection_sort(arr):
    for fillslot in range(len(arr)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if arr[location] > arr[positionOfMax]:
                positionOfMax = location

        temp = arr[fillslot]
        arr[fillslot] = arr[positionOfMax]
        arr[positionOfMax] = temp

    return arr

arr = [5,1,8,4,6,7]
print(selection_sort(arr))