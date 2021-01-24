class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m+j and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1[i+1:m+1+j] = nums1[i:m+j]
                nums1[i] = nums2[j]
                j += 1
                i += 1
                
        while j < n:
            nums1[m+j] = nums2[j]
            j+=1
            
        # while i < m+j:
        #     nums1[m+i] = nums1[i]
        #     i += 1

                

sol = Solution()
nums1 = [1,2,4,5,6,0]
nums2 = [3]
sol.merge(nums1, 5, nums2, 1)
print(nums1)

