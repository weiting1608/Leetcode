def countSort(arr):
    """
    Counting sort is used when there are smaller integers with multiple counts.
    Time complexity: O(n+k), Space complexity: O(k) for the counts array
    Strength: linear time; weakness: restricted inputs and space cost
    """
    maxVal = max(arr)
    output = [0] * len(arr)
    counts = [0] * (maxVal+1)

    for item in arr: # O(n)
        counts[item] += 1

    for i in range(1,len(counts)): # O(k) k is the range of integer
        counts[i] += counts[i-1]

    for item in arr: # O(n)
        counts[item] -= 1
        output[counts[item]] = item
    
    for i in range(len(arr)): # O(n)
        arr[i] = output[i]

    return arr

arr = [5,6,8,9,6,5,3,2,3,2,3,1,3,2,4]
print(countSort(arr))