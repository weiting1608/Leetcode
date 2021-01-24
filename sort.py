def bubblesort(arr):
    for n in range(len(arr)-1,0,-1):
        for i in range(n):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]

    return arr

def selectionsort(arr):
    for n in range(len(arr)-1, 0, -1):
        maxPos = 0
        for i in range(n+1):
            if arr[i] > arr[maxPos]:
                maxPos = i
        
        arr[n], arr[maxPos] = arr[maxPos], arr[n]

    return arr

def insertionsort(arr):
    for i in range(1, len(arr)):
        pos = i
        val = arr[i]
        while pos > 0 and arr[pos-1] > val:
            arr[pos] = arr[pos-1]
            pos -= 1

        arr[pos], arr[i] = arr[i], arr[pos]

    return arr

def shellsort(arr):
    sublist = len(arr)//2
    while sublist > 0:
        for start in range(sublist):
            insertionsortgap(arr, start, sublist)

        sublist = sublist // 2
    return arr

def insertionsortgap(arr, start, gap):
    for i in range(start+gap, len(arr), gap):
        pos = i
        val = arr[i]
        while pos >= gap and arr[pos-gap] > val:
            arr[pos] = arr[pos-gap]
            pos -= gap
        
        arr[pos], arr[i] = arr[i], arr[pos]

    return arr

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i, j = 0, 0
        arr[:] = []

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr.append(lefthalf[i])
                i += 1
            else:
                arr.append(righthalf[j])
                j += 1

        while i < len(lefthalf):
            arr.append(lefthalf[i])
            i += 1

        while j < len(righthalf):
            arr.append(righthalf[j])
            j += 1

    return arr

def quicksort(arr):
        
    quicksorthelper(arr, 0, len(arr)-1)
    return arr

def quicksorthelper(arr,low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksorthelper(arr, low, pi-1)
        quicksorthelper(arr, pi+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        else:
            j += 1
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

    
arr = [4,3,2,6,1,5,9,8]
print(bubblesort(arr))
print(selectionsort(arr))
print(insertionsort(arr))
print(shellsort(arr))
print(mergesort(arr))
print(quicksort(arr))