# Approach 1: brute force
# Time complexity: O(n^3), O(n^2 for every subarray), O(n) for sum calculation
# Space complexity: O(1)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for start in range(len(nums)):
            for end in range(start+1, len(nums)):
                subarray = nums[start:end+1]
                if sum(subarray) == k:
                    count += 1

        return count

# Approach 2: build a cumulative sum array
# This way, the sum of elements for the subarray nums[i:j], equals to sum[j+1]-sum[i]
