class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31-1 or x < -2**31:
            return 0
        else:
            if x >= 0:
                rev = int(str(x)[::-1])
            if x < 0:
                rev = -1 * int(str(x*(-1))[::-1])
            if rev not in range(-2**31, 2**31):
                return 0
            else:
                return rev
        