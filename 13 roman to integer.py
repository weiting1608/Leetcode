class Solution:
    def romanToInt(self, s: str) -> int:
        """
        need to ask the interview whether the input is valid or not
        """
        # Approach 1: lef-to-right pass
        values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        sums = 0
        i = 0
        while i < len(s):
            # substractive case
            if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
                sums += values[s[i+1]] - values[s[i]]
                i += 2
                
            else:
                sums += values[s[i]]
                i += 1
                
        return sums
        
        # Approach 2: lef-to-right improved
        values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "CM" : 900,
            "CD" : 400,
            "XC" : 90,
            "XL" : 40,
            "IX" : 9,
            "IV" : 4
        }
        
        sums = 0
        i = 0
        while i < len(s): # avoid index out of range
            # substractive case
            if i < len(s) -1 and s[i] + s[i+1] in values:
                sums += values[s[i]+s[i+1]]
                i += 2
                
            else:
                sums += values[s[i]]
                i += 1
                
        return sums
        

        # right-to-left pass
        values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        # Approach 3: right-to-left pass
        last = len(s)-1
        sums = values[s[last]]
        for i in reversed(range(len(s) - 1)):
            if values[s[i+1]] > values[s[i]]:
                sums -= values[s[i]]
            else:
                sums += values[s[i]]
                
        return sums