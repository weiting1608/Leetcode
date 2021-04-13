"""
Edge cases:
beginWord != endWord and beginWord, endWord not None
only lowercase
no duplicates in the word list
"""
# improved version of my naive approach
# Time complexity: O(26 * M * N), M is length of each word and N total number of words in wordset.
# Space complexity: O(M*N)


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0

        def neighbors(word, wordset):
            nei = []
            for i in range(len(word)):
                for c in range(ord('a'), ord('z')+1):
                    temp = word[:i] + chr(c) + word[i+1:]
                    if temp in wordset:
                        nei.append(temp)

            return nei

        que = collections.deque([(beginWord, 0)])
        seen = {beginWord}

        while que:
            word, step = que.popleft()
            if word == endWord:
                return step+1
            for nei in neighbors(word, wordset):
                if nei not in seen:
                    seen.add(nei)
                    que.append((nei, step+1))

        return 0

# My naive approach BFS: TLE(when wordList is long, find neighbors TLE)


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def neighbors(word, wordList):
            nei = []
            for w in wordList:
                count = 0
                for i in range(len(word)):
                    if word[i] != w[i]:
                        count += 1
                        if count > 1:
                            break
                if count == 1:
                    nei.append(w)
            return nei

        que = collections.deque()
        que.append((beginWord, 0))
        seen = set()
        seen.add(beginWord)

        while que:
            word, step = que.popleft()
            if word == endWord:
                return step+1
            for nei in neighbors(word, wordList):
                if nei not in seen:
                    seen.add(nei)
                    que.append((nei, step+1))

        return 0
