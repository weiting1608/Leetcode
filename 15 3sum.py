class Solution:
    def threeSum(self, nums):
        # Approach 1: two pointers and two sum of sorted array
        self.res = []
        
        nums.sort()
        
        for i in range(len(nums)-2):
            # sorted array, the nums after i are all greater than nums[i].
            if nums[i] > 0: break
            # skip the repetition of the same element, i == 0 is for dealing with i-1 out of index.
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i)
        return self.res
        
    def twoSum(self,nums, i):
        lo = i+1
        hi = len(nums)-1
        
        while(lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1      
            elif sum > 0:
                hi -= 1
            else:
                self.res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                # to remove the duplicates triplets
                while lo < hi and nums[lo] == nums[lo-1]: lo += 1


        # Approach 2: hash table
        # focus on Approach 1: easy to understand and implement
        res = []
        found, dups = set(), set()
        seen = {}
        
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        min_val = min((val1, val2, complement))
                        max_val = max((val1, val2, complement))
                        if (min_val, max_val) not in found:
                            found.add((min_val, max_val))
                            res.append([val1, val2, complement])
                    seen[val2] = i
        return res

sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(sol.threeSum(nums))