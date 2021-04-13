class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = list(range(1, n+1))

        def dfs(nums, stack):
            if len(stack) == k:
                res.append(stack[:])
            for i in range(len(nums)):
                stack.append(nums[i])
                newNums = nums[i+1:]
                dfs(newNums, stack)
                stack.pop()

        dfs(nums, [])
        return res
