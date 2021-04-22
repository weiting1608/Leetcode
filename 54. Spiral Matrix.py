# time complexity: O(m*n), we go through every element in the matrix for the answer.
# space complexity: O(1) no extra space is used for the computation.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        output = []
        dirs = 0
        
        while left <=right and top <= bottom:
            if dirs % 4 == 0:
                for i in range(left, right+1):
                    output.append(matrix[top][i])
                dirs += 1 
                top += 1

            elif dirs % 4 == 1:
                for i in range(top, bottom+1):
                    output.append(matrix[i][right])
                dirs += 1
                right -= 1


            elif dirs % 4 == 2:
                for i in range(right, left-1, -1):
                    output.append(matrix[bottom][i])
                dirs += 1
                bottom -= 1

            else:
                for i in range(bottom, top-1, -1):
                    output.append(matrix[i][left])
                dirs += 1
                left += 1
                
        return output
        