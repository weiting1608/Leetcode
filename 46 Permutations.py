class Solution:
    def permute(self, nums):
        self.res = []
        
        def dfs(nums, temp):
            if len(temp) == len(nums):
                # avoid the following change steps to affect the result
                self.res.append(temp[:]) # cann't be deep copy, but shallow copy
            
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                dfs(nums, temp)
                temp.pop()
                
        dfs(nums,[])
        return self.res