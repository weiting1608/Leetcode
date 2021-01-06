nums = [1,3,2]
i = 1
nums[i:] = nums[i:][::-1]
print(nums)