# divide and conquer
# pivot value and split point are two important concepts

def quick_sort(arr):
    
    quick_sort_helper(arr,0,len(arr)-1)
    return arr

def quick_sort_helper(arr,first,last):
    # split the array into partitions according to pivot value
    if first < last:
        splitpoint = partition(arr,first,last)
        # recursively sort subarrays for leftside and rightside.
        quick_sort_helper(arr,first,splitpoint-1)
        quick_sort_helper(arr,splitpoint+1,last)

def partition(arr,first,last):
    pivotvalue = arr[first]
    leftmark = first + 1
    rightmark = last
    
    done = False
    
    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark += 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        
        else:
            # swap the value in leftmark with rightmark

            arr[leftmark],arr[rightmark] = arr[rightmark],arr[leftmark]

    # swap the pivot value(first) with the rightmark value
    # after this, except for pivot value, all value on the leftside is smaller 
    # than pivot value, and all value on the rightside is larger than pivot.
    arr[first],arr[rightmark] = arr[rightmark],arr[first]

    return rightmark

arr = [16,24,3,20]
print(quick_sort(arr))
