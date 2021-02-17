class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Approach 1: Kadane's algorithm
        # Time complexity O(n), go through the array once.
        maxSum, curSum = nums[0], 0
        for i in range(1, len(nums)):
            if curSum < 0: 
                curSum = 0
                start = i
            curSum += nums[i]
            if curSum > maxSum:
                maxSum = curSum
                end = i
                
        # print the maximum subarray
        print(nums[start: end+1])
        
        return maxSum


        # Similar to Approach 1: dp
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            if dp[i-1] + nums[i] < nums[i]:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
                
        return max(dp)


        # Approach 2: divide and conquer
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        pivot = len(nums) // 2
        leftMax = self.maxSubArray(nums[:pivot])
        rightMax = self.maxSubArray(nums[pivot:])
        centerMax = self.maxCenter(nums, pivot)
        return max(leftMax, rightMax, centerMax)
    
    def maxCenter(self, nums, pivot):
        maxLeft, maxRight = nums[pivot-1], nums[pivot]
        sumLeft, sumRight = 0, 0
        for i in range(pivot-1, -1, -1):
            sumLeft += nums[i]
            maxLeft = max(maxLeft, sumLeft)
        for i in range(pivot, len(nums)):
            sumRight += nums[i]
            maxRight = max(maxRight, sumRight)
            
        return maxLeft+maxRight
            
            
        