class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [""]
        for s in S:
            if s.isalpha():
                res = [word + j for word in res for j in [s.lower(), s.upper()]]
            else:
                res = [word + s for word in res]
        return res

# too complicated
# class Solution:
#     def letterCasePermutation(self, S):
#         ans = [[]]
        
#         for char in S:
#             n = len(ans)
#             if char.isalpha():
#                 for i in range(n):
#                     ans.append(ans[i][:])
#                     ans[i].append(char.lower())
#                     ans[n+i].append(char.upper())
            
#             else:
#                 for i in range(n):
#                     ans[i].append(char)
                    
#         return map("".join, ans)
        
sol = Solution()
print(sol.letterCasePermutation("a4c"))