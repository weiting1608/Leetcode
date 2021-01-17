class Solution:
    def search(self, nums, target):
        if len(nums) == 0: return -1
        left, right = 0, len(nums)-1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] > target:
                right = pivot - 1
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                return pivot
            
        return -1
        
        

sol = Solution()
print(sol.search([-1,0,3,5,9,12], 9))
        
        