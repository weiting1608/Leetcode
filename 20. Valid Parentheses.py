class Solution:
    def isValid(self, s: str) -> bool:
        par_start = set('([{')
        matches = set([('(',')'),('[',']'),('{','}')])
        stack = []
        if len(s) == 0: return True
        if len(s)%2 != 0: return False
        for par in s:
            if par in par_start:
                stack.append(par)
            else:
                if len(stack) == 0: return False
                last_open = stack.pop()
                if (last_open, par) not in matches:
                    return False
                
        return len(stack) == 0
                
                
                
        