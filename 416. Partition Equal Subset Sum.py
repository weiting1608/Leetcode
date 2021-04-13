# knapsack problem https://leetcode.com/problems/partition-equal-subset-sum/solution/
#! video solution is amazing!!!!!

# Approach 1: brute force -- recursion, for each num in nums, decide whether to choose
# the num to get a sum equals to total // 2
# Time complexity: O(2^n)
# Space complexity: O(n)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        def recursion(nums, idx, remain):
            if remain == 0:
                return True
            if remain < 0 or idx == len(nums):
                return False
            return recursion(nums, idx+1, remain) or recursion(nums, idx+1, remain-nums[idx])

        return recursion(nums, 0, total // 2)


# Approach 2: recursion with memo, TLE still
# Time complexity: the number of the unique subproblems, in the worst case, O(mn)
# Space complexity: O(mn)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        remain = total // 2
        memo = [[None for _ in range(remain+1)] for _ in range(len(nums)+1)]

        def recursion(nums, idx, remain):
            if remain == 0:
                return True
            if remain < 0 or idx == len(nums):
                return False
            if memo[idx][remain]:
                return memo[idx][remain]

            res = recursion(nums, idx+1, remain) or recursion(nums,
                                                              idx+1, remain-nums[idx])
            memo[idx][remain] = res
            return res

        return recursion(nums, 0, remain)

# Approach 3: dynamic programming
# Time complexity: O(mn)
# Space complexity: o(m) using only 1D dp array, traverse from right to left
# If forgot how it works, check the video solution.


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        n = len(nums)
        total //= 2
        dp = [False for _ in range(total+1)]

        dp[0] = True

        for i in range(n-1, -1, -1):
            for j in range(total, -1, -1):
                if j < nums[i]:
                    continue
                dp[j] = dp[j] or dp[j-nums[i]]

        return dp[total]
