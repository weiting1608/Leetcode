class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))

        subsets = []

        def dfs(nums, stack):
            if len(stack) == k and sum(stack) == n:
                subsets.append(stack[:])
            for i in range(len(nums)):
                stack.append(nums[i])
                newNums = nums[i+1:]
                dfs(newNums, stack)
                stack.pop()

        dfs(nums, [])

        return subsets
