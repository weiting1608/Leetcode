class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, stack):
            if not nums:
                res.append(stack)
            for i in range(len(nums)):
                stack.push(nums[i])
                newNums = nums[:i] + nums[i+1:]
                print(newNums)
                dfs(newNums, stack)
                stack.pop()

        dfs(nums, [])
