class Solution:
    def trap(self, height):
        # Approach 1: brute force Time complexity o(n^2), space complexity o(1)
        if len(height) < 2: return 0
        res = 0
        for i in range(1, len(height)-1):
            left_max = height[0]
            right_max = height[-1]
            left_max = max(max(height[:i]), left_max) 
            right_max = max(max(height[i+1:]),right_max)
            temp = min(left_max, right_max) - height[i]
            if temp > 0: res += temp
        return res

        # Approach 2: two pointers Time complexity o(n), space complexity o(1)
        if len(height) < 2: return 0
        res = 0
        # two pointers left and right
        left, right = 0, len(height)-1
        left_max, right_max = 0, 0
        while left < right:
            # meaning that the water trapped depends on the short bar, so update the left part.
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else: res += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else: res += right_max - height[right]
                right -= 1
        return res
        
sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))            