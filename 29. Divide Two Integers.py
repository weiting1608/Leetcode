class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp = 1
            div = divisor
            while (div << 1) <= dividend:
                div <<= 1
                temp <<= 1
            dividend -= div
            res += temp
        # deal with negative case
        res = -res if neg else res
        # deal with the overflow case
        return max(-2**31, min(res, 2**31-1))
            
            