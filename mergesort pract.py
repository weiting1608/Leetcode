def mergeSort(arr):
    if len(arr) == 1: return arr

    else:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        lefthalf = mergeSort(lefthalf)
        righthalf = mergeSort(righthalf)

        i, j = 0, 0
        res = []
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                res.append(lefthalf[i])
                i += 1
            else:
                res.append(righthalf[j])
                j += 1

        while i < len(lefthalf):
            res.append(lefthalf[i])
            i += 1
        
        while j  < len(righthalf):
            res.append(righthalf[j])
            j += 1

        return res

arr = [2,1,4,3,6754,2,324,643,5]
print(mergeSort(arr))
