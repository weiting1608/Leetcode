class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(nums, stack, k):
            if len(stack) == k and stack not in res:
                res.append(stack[:])
            for i in range(len(nums)):
                stack.append(nums[i])
                newNums = nums[i+1:]
                dfs(newNums, stack, k)
                stack.pop()

        for i in range(len(nums)+1):
            dfs(nums, [], i)

        return res
