# Approach 1: naive recursion
# Time complexity: given a string of length n, there are n+1 ways to split into two parts,
# for each step, we have a choice, split or not split
# when all choices are to be checked, it is O(2^n)
# Space complexity: O(n) The depth of the recurion tree can go upto n.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def recursion(s, wordDict, start):
            # traverse the string s, until start reaches the end of the word
            # meaning all s[start:end] in wordDict, return True
            # base case
            if start == len(s):
                return True

            # since end will not be consider in substring,
            # so here len(s)+1 is necessary to check the last character
            for end in range(start+1, len(s)+1):
                # traverse end until s[start: end] is found in wordDict and check the rest start from end
                # using the recursion helper function
                if s[start:end] in wordDict and recursion(s, wordDict, end):
                    return True

            return False

        return recursion(s, wordDict, 0)

# Approach 2: recursion with memo
# Time complexity: O(n^3) size of recursion tree can go upto n^2
# Space complexity: O(n), the depth of recursion tree.


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def recursion(s, wordDict, start):
            if start == len(s):
                return True

            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict and recursion(s, wordDict, end):
                    return True

            return False

        # using frozenset (immutable set) is necessary
        return recursion(s, frozenset(wordDict), 0)

# Approach 3: dynamic programming
# Time complexity: O(n^3) two nested loop, and substring computation at each iteration
# Space complexity: O(n), length of dp array


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False for _ in range(len(s)+1)]
        # base
        dp[0] = True

        for i in range(1, len(s)+1):  # i denotes end(exclusive)
            for j in range(i):  # j denotes start
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    # save checking other j splitting point
                    break

        return dp[len(s)]
