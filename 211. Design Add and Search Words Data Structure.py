# Approach 1: use dictionary
from collections import defaultdict


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.d[len(word)].add(word)

    def search(self, word: str) -> bool:
        m = len(word)
        for wordDict in self.d[m]:
            i = 0
            while i < m and (wordDict[i] == word[i] or word[i] == '.'):
                i += 1
            if i == m:
                return True

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Approach 2: use trie -- dynamic dictionary implementation
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie

        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = True

    def search(self, word: str) -> bool:
        def searchInNode(word, node):
            for i, c in enumerate(word):
                if c not in node:
                    if c == '.':
                        for key in node:
                            if key != '#' and searchInNode(word[i+1:], node[key]):
                                return True
                    return False
                else:
                    node = node[c]
            return '#' in node
        return searchInNode(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
