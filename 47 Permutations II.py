class Solution:
    def permuteUnique(self, nums):
        self.res = []
        self.used = [False] * len(nums)
        
        def dfs(nums, temp):
            if len(temp) == len(nums):
                self.res.append(temp[:])
                
            for i in range(len(nums)):
                if self.used[i]: continue
                #self.used[i-1] should be true, means i-1 went to the dfs
                if i>0 and nums[i] == nums[i-1] and self.used[i-1]: continue
                self.used[i] = True
                temp.append(nums[i])
                dfs(nums, temp)
                self.used[i] = False
                temp.pop()
                
        dfs(sorted(nums), [])
        return self.res