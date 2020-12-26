import itertools as it

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs', '8':'tuv','9':'wxyz'}
        letter_list = []
        for i in range(len(digits)):
            if digits[i] not in dic:
                return ''
            if digits[i] in dic:
                letter_list.append(dic.get(digits[i]))
        
        return [''.join(i) for i in it.product(*letter_list) if i]
                

        
        
                                         
