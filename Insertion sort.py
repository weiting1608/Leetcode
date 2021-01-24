def insertionSort(arr):
    # fits well for nearly sorted array

    # for every new ele, actually start from the 2nd ele. range(1,len(arr))
    for pos, currentVal in enumerate(arr):

        # end when the appropriate position for the currentVal is found, therefore while instead of "for"
        while pos > 0 and arr[pos-1] > currentVal:
            # make room for the currentVal, move the large value one space behind
            arr[pos] = arr[pos-1]
            pos -= 1
        
        # put the currentVal to its appropriate position
        arr[pos] = currentVal
    return arr


arr = [1,4,2,3,6,7]
print(insertionSort(arr))