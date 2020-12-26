class Solution:
    def twoSum(self, nums, target):
        
        dic = {}
        for i, num in enumerate(nums):
            val = target - num
            if val not in dic:
                dic[num] = i # used for add kv pair to dict
            else:
                return[dic[val],i]

sol = Solution()
array = [3,2,6,1,9]
print(sol.twoSum(array, 3))