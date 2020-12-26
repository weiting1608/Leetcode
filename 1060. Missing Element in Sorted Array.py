class Solution:
    def missingElement(self, nums, k):
        # Approach 2: binary search
        if len(nums) <= 1: return
        
        missing = lambda x: nums[x]-nums[0]-x
        
        if k > missing(len(nums)-1):
            return nums[-1] + k - missing(len(nums)-1)
        
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if missing(mid) < k:
                l = mid + 1
            else:
                r = mid
        
        return nums[l-1] + k - missing(l-1)
        
        # Approach 1: one pass -- linear search
        # x = 1
        # while missing(x) < k:
        #     x += 1
        # return nums[x-1]+k-missing(x-1)
            
        # Original thoughts of myself: TLE
        # missing = []
        # count = 0
        # for i, num in enumerate(nums):
        #     while count < k  and num < nums[i+1]:
        #         if num+1 in nums: continue
        #         else: 
        #             missing.append(num+1)
        #             count += 1
        #             num += 1
        
        # return missing[k-1]

sol = Solution()
print(sol.missingElement([4,7,9,10],3))
        