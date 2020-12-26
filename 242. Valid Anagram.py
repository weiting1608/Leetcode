class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach 1: return sorted(s) == sorted(t)

        # Approach 2: put the indivual letter in []
        if len(s) != len(t): return False
        
        letters = []
        for i in range(len(s)):
            letters.append(s[i])
        
        for i in range(len(t)):
            if t[i] in letters:
                letters.remove(t[i])
        
        return letters == []

        # Approach 3: put individual letter in {}
        s = s.replace(' ','').lower()
        t = t.replace(' ','').lower()
        
        dic = {}
        for letter in s:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        
        for letter in t:
            if letter in dic:
                dic[letter] -= 1
            else:
                dic[letter] = 1
            
        for letter in dic:
            if dic[letter] != 0: return False
        
        return True        
            
        
            
        