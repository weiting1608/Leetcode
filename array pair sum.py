"""
Given an integer array, output all the unique pairs sum up to a specific value k.
So the input: pair_sum([1,3,2,2], 4) would return 2 pairs: (1,3) (2,2)
"""

class Solution:
    def pair_sum(self, arr, k):
        if len(arr) < 2:
            return

        # Sets for tracking
        seen = set()
        output = set()

        for num in arr:
            target = k-num
            if target not in seen:
                seen.add(num)           
            else:
                output.add((min(num, target), max(num, target)))            
        # return len(output)
        print('\n'.join(map(str,list(output))))
sol = Solution()
print(sol.pair_sum([1,3,2,2],4))