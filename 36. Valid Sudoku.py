class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isUnique(row): return False
        # nice trick to get the column using zip(*board)
        # * is known as unpacking operator
        for column in zip(*board):
            if not self.isUnique(column): return False
        
        sub_boxes = []
        for x_sub in range(3):
            for y_sub in range(3):
                sub_box = []
                for i in range(3):
                    for j in range(3):
                        sub_box.append(board[i+x_sub*3][j+y_sub*3])
                sub_boxes.append(sub_box)
        for sub_box in sub_boxes:
            if not self.isUnique(sub_box): return False
        return True
    
    
    def isUnique(self, array):
        dic ={}
        for i in array:
            if i != '.': 
                # typical way for getting the frequence of the value
                dic[i] = dic.get(i,0)+1 
            
        for value in dic.values():
            if value > 1: return False
            
        return True