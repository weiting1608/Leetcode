"""
consider an array of non-negative integers. A second array is formed by shuffling the 
elements of the first array and deleting a random element. Given these two arrays, 
find which element is missing in the second array.
example: finder([1,2,3,4,5,6,7], [3,7,2,1,4,6])
"""
import collections

def finder(arr1, arr2):

    # Approach 1: check one by one
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
    
    return arr1[-1]
 
    # Approach 2: hash table
    d = collections.defaultdic(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1
    
    # Approach 3: add the sum of both arr1 and arr2,
    # the difference between the sum is the missing elemnet.
    # problem of this method: when the list is too long, may come across with overflow.

    # Approach 4: using XOR
    result = 0
    # perform an XOR between the numbers in the arrays
    for num in arr1+arr2:
        result ^= num

    return result