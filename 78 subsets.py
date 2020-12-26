class Solution:
    def subsets(self, nums):
        # start with self. is the global variable
        # usually store the return value
        self.res =[]

        # temp is for storing the current subset
        def dfs(nums, temp, i):

            # need to use slice copy so that won't influence the original
            self.res.append(temp[:])
            for i in range(i, len(nums)):
                temp.append(nums[i])
                dfs(nums, temp, i+1)
                # pop is important
                temp.pop()
                
        dfs(nums, [], 0)
        return self.res

sol = Solution()
print(sol.subsets([1,2,3]))