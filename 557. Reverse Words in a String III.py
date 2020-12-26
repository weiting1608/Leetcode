557. Reverse Words in a String III
class Solution:
    def reverseWords(self, s: str) -> str:
        output = []
        words = s.split()
        for word in words:
            word = word[::-1]
            output.append(word)
               
        return " ".join(output)
        
# Other approach: one line code 
        return " ".join(i[::-1] for i in s.split())