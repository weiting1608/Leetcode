class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            acc = 0
            strX = str(x)
            for i in range(len(strX)//2):
                if strX[i] != strX[len(strX)-i-1]:
                    acc += 1
                    
            if acc!=0:
                return False
            else: 
                return True
                    
        # Or can take advantage of reverse string built-in function
        # one line code: return str(x) == str(x)[::-1]