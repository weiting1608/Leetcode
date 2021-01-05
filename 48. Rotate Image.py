class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose the matrix
        for i in range(len(matrix)):
            # For transpose, there is no need to exchange the diagonal element, so j starts from i+1
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i],  matrix[i][j]
                
        # reverse the transposed matrix
        for i in range(len(matrix)):
            # or use the built-in python of reverse a list: matrix[i].reverse()
            for k in range((len(matrix[0])//2)):
                matrix[i][k], matrix[i][len(matrix[0])-k-1] = matrix[i][len(matrix[0])-k-1], matrix[i][k]
        
sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[::-1])
# Because this rotate func return None type, so directly printing will give you None.
# sol.rotate is just an operation like reverse(), so first conduct it, and then print the existing list.
# It can't be combined together like print(sol.rotate(matrix)).
sol.rotate(matrix)
print(matrix)