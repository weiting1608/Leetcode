# in O(n) time and O(1) space
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        # put nums[i] to the correct place when nums[i] is in range[1,n]
        while i < n:
            j = nums[i]-1
            if 0 <= j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i+1:
                return i+1

        return n+1

# simpler version with more time complexity
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or 1 not in nums:
            return 1
        mx = max(nums)
        for i in range(1, mx+1):
            if i not in nums:
                return i
        return mx+1
