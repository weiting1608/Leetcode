def countInversion(arr, start, end):
    if start < end:
        mid = (start+end) // 2
        leftInversion = countInversion(arr, start, mid)
        rightInversion = countInversion(arr, mid+1, end)
        inversion = mergeInversion(arr, start, mid, end) + leftInversion + rightInversion
        return inversion

    else:
        return 0

def mergeInversion(arr, start, mid, end):
    leftLength = mid - start + 1
    rightLength = end - mid
    L, R = [0]*(leftLength+1), [0]*(rightLength+1)
    for i in range(0, leftLength):
        L[i] = arr[start+i]
    for j in range(0, rightLength):
        R[j] = arr[mid+j+1] 
    L[leftLength] = R[rightLength] = float('inf')

    i = j = 0
    inversion = 0
    for k in range(start, end+1):
    
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            inversion += leftLength-i
            arr[k] = R[j]
            j += 1
    return inversion

arr = [1,3,4,2,6]
print(countInversion(arr, 0, 4))
