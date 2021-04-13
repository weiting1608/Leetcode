class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        to test whether a number is the power of two.
        when it is the power of two, then the binary form only contains one '1'
        """
        if n <= 0:
            return False
        return bin(n).count('1') == 1
