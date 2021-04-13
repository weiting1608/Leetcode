# Approach 1: Bit by bit computation
# Time complexity(O(max(n, m))) n and m are the lengthes of the input strings
# Space complextiy(O(max(n, m))) to store the ans in array

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            return self.addBinary(b, a)

        b = b.zfill(len(a))
        print(b)
        carry = 0
        res = []
        for i in range(len(a)-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            digit = carry % 2
            carry = carry // 2
            if digit == '1':
                res.append('1')
            else:
                res.append('0')

        if carry:
            res.append('1')

        res = res[::-1]
        return "".join(res)

# Approach 2: bit manipulation


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            carry = (x & y) << 1
            ans = x ^ y
            x, y = ans, carry
        return bin(x)[2:]
