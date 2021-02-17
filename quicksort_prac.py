def quickSort(arr):
    quickSort_helper(arr, 0, len(arr)-1)
    return arr

def quickSort_helper(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSort_helper(arr, low, p-1)
        quickSort_helper(arr, p+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    # i stores the last index of the group which is less than the pivot value
    i = low - 1
    # j is used to track the value until it traverses all the element before the pivot value
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

arr = [1,23,645,3,2,45,734,4,78]
print(quickSort(arr))