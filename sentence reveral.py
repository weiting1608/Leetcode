class Solution():
    def rev_sen(self, s):
        words = []
        space = [' ']

        i = 0
        while i < len(s):
            if s[i] not in space:
                word_start = i
            while i < len(s) and s[i] not in space:
                i += 1
            words.append(s[word_start:i])

            i += 1

        return words

    def output(self, arr):
        rev_arr = []
        for i in range(len(arr)-1,-1,-1):
            rev_arr.append(arr[i])

        return ' '.join(rev_arr)

sol = Solution()
print(sol.output(sol.rev_sen("I am the prettiest.")))