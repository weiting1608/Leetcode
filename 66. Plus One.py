class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        lastInd = len(digits) - 1
        # need extra space for storing the calculated digits, otherwise will mess up around when doing // and %.
        res = []
        
        for i in range(lastInd, -1, -1):
            curr = (digits[i] + carry) % 10
            res.append(curr)
            carry = (digits[i] + carry) // 10
        
        # Deal the edge case of all 9's
        if carry == 1:
            res.append(carry)
        
        res.reverse()
        return res
                

            

                
                