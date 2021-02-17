def heapSort(arr):
    """
    Implementation of heap sort. Using heapify instead of insertion to build the maxheap.
    insertion to build the maxheap, time complexity: O(nlogn), same as deletion.
    heapify to build the maxheap, time complexity: O(n).
    However, 2 steps are needed:
    1. build the maxheap
    2. delection the largest value from the heap. O(nlogn)
    Therefore, the general time complexity is still O(nlogn).
    """
    n = len(arr)

    # Build a maxheap, only cares the non-leaf nodes, 'cause the leaf node itself is heapified one.
    # non-leaf nodes starts from n//2-1 in the case that index starts from 0.
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
    
    # Deletion of the max, first swap the maximum value to the end, and then heapify the rest.
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)                                           
    
    return arr

def heapify(arr, n, i):
    largest = i # initialize the largest as root
    l = 2 * i + 1 # left child index
    r = 2 * i + 2 # right child index

    # find the largest value among root, left child, right child.
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    # swap the largest to the root
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        # starts from the largest(either left/right child, make sure the rest are maxheap)
        heapify(arr, n, largest)
    
arr = [6,5,3,8,9,1,2]
print(heapSort(arr))
