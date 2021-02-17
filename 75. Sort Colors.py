class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach 1: use the counting sort algorithm, need extra space for store the array.
        count = [0] * 3
        output = [0] * len(nums)
        for num in nums:
            count[num] += 1
        for i in range(1, len(count)):
            count[i] += count[i-1]
        for num in nums:
            count[num] -= 1
            output[count[num]] = num
        for i in range(len(nums)):
            nums[i] = output[i]
        
        # Approach 2: hash map
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        nums[:] = []
        for i in range(3):
            if i in count:
                for _ in range(count[i]):
                    nums.append(i)

        # Approach 3: no extra space, use pointers
        start, end = 0, len(nums)-1
        for i in range(len(nums)):
            while nums[i] == 2 and i < end:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
            while nums[i] == 0 and i > start:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
        