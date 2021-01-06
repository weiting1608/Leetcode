class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # flag is used for the case that the whole list is the last permutation.
        flag = 1
        # i should be terminated at position 1, need to make sure that i-1 within the range.
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]: 
                j = len(nums)-1
                # Should consider the equal condition. Otherwise it doesn't make sense of swap two equal values.
                while nums[j] <= nums[i-1]:
                    j -= 1

                nums[j], nums[i-1] = nums[i-1], nums[j]
                flag = 0
                break
        if flag: nums.reverse()
        # The way of nums[i:].reverse() doesn't work. reverse() works only on whole list.
        # For reverse of sliced list, using [::-1].
        else: nums[i:] = nums[i:][::-1]
