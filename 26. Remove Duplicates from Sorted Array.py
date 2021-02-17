class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # use slow to mark the end of the new, non-duplicate array
        # use fast to traverse the array.
        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow+1
                