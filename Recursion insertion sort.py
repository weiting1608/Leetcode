def recurInsertionSort(arr, n):
    if n > 1:
        recurInsertionSort(arr, n-1)
        insert(arr, n)

def insert(arr, k):
    val = arr[k]
    i = k-1
    while i > 0 and arr[i] > val:
        arr[i+1] = arr[i]
        i -= 1

    arr[i+1] = val


arr = [6,3,2,5,1]
n = len(arr)
print(recurInsertionSort(arr,n))
