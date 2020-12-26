#using divide and conquer strategy
#divide the whole list into small list until only element in that list
#merge the small list level by level

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0 # for left half
        j = 0 # for right half
        k = 0 # for the final arr

        # when there are elements left in both lefthalf and righthalf
        while i < len(lefthalf) and j < len(righthalf):

            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]

                i +=1

            else:
                arr[k] = righthalf[j]
                j += 1

            k += 1

        # when all elements from either left or right has been put into the
        # right position and nothing left to compare, here just to put the rest
        # element of one array in the final array
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
        
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

    return arr

arr = [23,432,15,2,7,2121,48]
print(merge_sort(arr))
