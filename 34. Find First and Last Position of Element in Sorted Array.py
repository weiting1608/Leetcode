class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Approach 1: linear search
        if target not in nums: return [-1, -1]
        start, end = 0,0 
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                break
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target: 
                end = j
                break
            
        return [start, end]

        # Approach 2: binary search time complexity O(logn)
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end)//2 
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            # Under normal situation, the target value has been found out.
            # But here there are multiple target values, so checking the start and end is needed.
            else:
                start = mid
                while start >= 0 and nums[start] == target: 
                    start -= 1
                end = mid
                while end < len(nums) and nums[end] == target:
                    end += 1
                return [start+1, end-1]
        return [-1, -1]
                    
                
        