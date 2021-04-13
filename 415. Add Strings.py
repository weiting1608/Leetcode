class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            return self.addStrings(num2, num1)

        num2 = num2.zfill(len(num1))
        carry = 0
        res = []
        for i in range(len(num1)-1, -1, -1):
            tempSum = int(num1[i]) + int(num2[i]) + carry
            digit = tempSum % 10
            carry = tempSum // 10
            res.append(str(digit))

        if carry:
            res.append(str(carry))

        if len(res) <= 1:
            return res[0]
        else:
            res.reverse()
            return "".join(res)
