class Solution():
    def lengthOfLongestSubstring(self, s: str) -> int:
    #     """
    #     Brute Force:
    #     1. enumerate all substring of strings;
    #     2. check whether the substring is not repeating;
    #     3. return the longest non-repeating substring
    #     Time Complexity: O(n^3): 
    #     for each fixed substring (i to j): search all elements unique
    #     then for each i and each j, search another round.
    #     Space Complexity: (O(min(n,m)))
    #     """
    #     str_len = len(s)
    #     result = 0
    #     for i in range(str_len):
    #         # j is not the index, but the one behind that, 'cause in def allUnique i in range(start, end)
    #         for j in range(i+1,str_len+1):
    #             if(self.allUnique(s,i,j)):
    #                 result = max(result, j-i)
                    
    #     return result
    
    # def allUnique(self, s, start, end):
    #     set_str = set()
    #     for i in range(start, end):
    #         ch = s[i]
    #         if ch in set_str:
    #             return False
    #         set_str.add(ch)
            
    #     return True

        """
        HashMap
        """
        # Approach 2: hashmap
        dicts = {}
        result = start = 0
        for i, value in enumerate(s):
            # For character already in dicts
            # update the start from the element behind this existing char
            if value in dicts:
                update_start = dicts[value] + 1
                if update_start > start: # to make sure the start won't roll back, consider the case of "abba"
                    start = update_start
            
            num = i - start + 1
            if num > result:
                result = num
            # this step is for adding the new pairs to the dictionary. Important!!!
            # or to update the i for existing value.
            dicts[value] = i
            
        return result

        # Approach 3: sliding window
        if len(s) <= 1: return len(s)
        charSet = set()
        left, res = 0, 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            res = max(res, right - left + 1)
            
        return res
        


sol = Solution()
print(sol.lengthOfLongestSubstring("abba"))