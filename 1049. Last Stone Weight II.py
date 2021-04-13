class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def backtrack(i, l, r):
            if i == len(stones):
                return abs(l-r)
            return min(backtrack(i+1, l+stones[i], r), backtrack(i+1, l, r+stones[i]))
        return backtrack(0, 0, 0)
