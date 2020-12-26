class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        row = 0
        zigzag = ['' for x in range(numRows)]
        
        for char in s:
            zigzag[row] += char
            
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
                
            row += step
            
        return ''.join(zigzag)

sol = Solution()
print(sol.convert("ILOVEJOE", 4))