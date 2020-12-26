class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Approach 1: two pointers
        # left, right = 0, len(s)-1
        # while left<right:
        #     s[left], s[right] = s[right],s[left]
        #     left += 1
        #     right -= 1
        
        # Approach 2: improved version, no need for two pointers
        # only need to change the half part
        for i in range(len(s)//2):
            j = len(s)-1-i
            s[i],s[j] = s[j],s[i]
            i+=1