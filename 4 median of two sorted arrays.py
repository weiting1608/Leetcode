class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        imin, imax, half_len = 0, len(nums1), (len(nums1)+len(nums2)+1)//2
        while imin <= imax:
            i = (imin+imax)//2
            j = half_len-i
            # last element of nums2(left partition) > first element of nums1(right partition)
            # i is too small, needs to move towards right
            if i < len(nums1) and nums2[j-1] > nums1[i]:
                imin = i + 1
            # i is too big, needs to move towards left
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            # i is perfect, no need to move
            else:
                if i == 0:
                    left_max = nums2[j-1]
                elif j == 0:
                    left_max = nums1[i-1]
                else:
                    left_max = max(nums1[i-1], nums2[j-1])

                if (len(nums1)+len(nums2)) % 2 == 1:
                    return left_max

                if i == len(nums1):
                    right_min = nums2[j]
                elif j == len(nums2):
                    right_min = nums1[i]
                else:
                    right_min = min(nums1[i], nums2[j])

                return (left_max + right_min) / 2


sol = Solution()
nums1 = [1, 3, 5, 9]
nums2 = [2, 7, 9, 10]
print(sol.findMedianSortedArrays(nums1, nums2))
