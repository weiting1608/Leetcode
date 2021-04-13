def meanderingArr(arr):
    arr.sort()
    meandering = []
    n = len(arr)
    mid = n // 2
    for i in range(mid):
        meandering.append(arr[n-1-i])
        if n-1-i != i:
            meandering.append(arr[i])

    if n % 2 == 1:
        meandering.append(arr[mid])

    return meandering


arr = [-1, 1, 2, 3, -5]
print(meanderingArr(arr))
