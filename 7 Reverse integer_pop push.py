class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        int_max = 2 ** 31-1
        int_min = -2 **31
        while(x > 0):
            pop = x % 10
            x //= 10
            if(rev > int_max//10 or (rev == int_max//10 and pop > 7)): return 0
            rev = rev * 10 + pop
        while(x < 0):
            pop = -((-x) % 10)
            x = -((-x) // 10)
            if(rev < -((-int_min)//10) or (rev == -((-int_min)//10) and pop < -8)): return 0
            rev = rev * 10 + pop
        return rev
        
# Notice the difference that the negative number come across with % and // operator
sol = Solution()
print(sol.reverse(-321))