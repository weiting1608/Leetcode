class Solution:
    # time complexity: O(logN)
    # space complexity: O(1)
    def mySqrt(self, x: int) -> int:
        l, r = 0, x+1
        while l < r:
            mid = (l + r) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                l = mid + 1
            else:
                r = mid

        return l-1
