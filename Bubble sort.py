def bubble_sort(arr):
    # n is used for the boundary of k.
    for n in range(len(arr)-1, 0, -1):
        # for each pass, only check the first nth ele, because the n+1 th to last ele has already in the right place.
        for k in range(n):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]

    return arr

arr = [5,3,7,2]
print(bubble_sort(arr))
