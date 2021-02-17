def bucketSort(arr):
    """
    Time complexity: Best O(n+k), Average O(n+k), Worst O(n^2)
    """
    arr_helper = []
    slot_num = 10
    # step 1: build a helper with 10 buckets
    for i in range(slot_num):
        arr_helper.append([])
    
    # step 2: put elements in different bucket
    for j in arr:
        index = int(slot_num * j)
        arr_helper[index].append(j)

    # step 3: sort the individual buckets using insertion sort
    for i in range(slot_num):
        arr_helper[i] = insertionSort(arr_helper[i])

    # step 4: concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr_helper[i])):
            arr[k] = arr_helper[i][j]
            k += 1
    return arr

def insertionSort(arr):
    for i in range(1, len(arr)):
        pos = i
        val = arr[i]

        while pos > 0 and arr[pos-1] > val:
            arr[pos] = arr[pos-1]
            pos -= 1
        
        arr[pos] = val

    return arr

arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print(bucketSort(arr))