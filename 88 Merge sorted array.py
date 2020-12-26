class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # Approach 1: merge and sort
        # Time complexity: (m+n)log(m+n)
        # Space complexity: O(1)
        # Doesn't take advange of the two array has been sorted already
        # nums1[:] = sorted(nums1[:m] + nums2)

        # Approach 2: two pointers
        # Time complexity: o(n+m)
        # Space complexity: O(m) used for store the element in nums1
        nums1_copy = nums1[:m]
        nums1[:] = []

        #two get pointers for nums1_copy and nums2
        p1 = 0
        p2 = 0

        #compare elements from nums1_copy and nums2
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # if there are still elements to add
        while p1 < m:
            nums1.append(nums1_copy[p1])
            p1 += 1

        while p2 < n:
            nums1.append(nums2[p2])
            p2 += 1


        

sol = Solution()
nums1 = [2,6,9,10,0,0,0,0,0]
nums2 = [1,3,5,7,8]
sol.merge(nums1,4,nums2,5)
print(nums1)