class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Approach 1: brute force (time limited)
        max_area = 0
        for i in range(0, len(height)):
            for j in range(len(height)-1, i, -1):
                max_area = max(max_area, (j-i) * min(height[i],height[j]))
        
        return max_area

        # Approach2 : two pointers
        # first pointer: the beginning
        # second pointer: the end
        """ 
        In the initial state, the length is the largest. Then moving inwards the shorter line 
        ('cause inwards the longer line won't increase the area)
        Tho the length is reduced by 1, but there is possiblity that the height will be larger, so may get a larger area.
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        while(left < right):
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
        