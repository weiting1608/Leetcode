### !!!! Frequently asked.

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Approach 1: two pointers, old & new state.
        # 1. cur_result is calculated based on old_state and cur_element of the sequence.
        # 2. before assigning cur_result to new_state, store the value of the new_state to old_state first.
        # 3. regard cur_result as the new_state.

        # last is used for storing the old state (n-2).
        # now is used for updating the result (n-1).
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last + num, now)
        return now

        # Approach 2: dp
        # base case
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[n-1]
        
        