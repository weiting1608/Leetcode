# Approach 1: using dynamic dictionary, special feature of python. can't use in java/c++
# For the case inserting "app", the structure is like {'a': {'p': {'p': {'#': True}}}}
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p["#"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.find(word)
        return node is not None and '#' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.find(prefix)
        return node is not None

    def find(self, prefix):
        p = self.root
        for c in prefix:
            if c not in p:
                return None
            p = p[c]
        return p

# Approach 2: conventional one
# Pay attention to build a class TrieNode, and define the attributes of TrieNode(isWord and children array)
# use object TrieNode (contains boolean attribute: isWord and an array 'children' [None] * 26 to store the following children)
# difference to 1st approach, 1st is dictionary of dictionary
# this is object (boolean, array) of object(boolean array)


class Trie:
    class TrieNode():
        def __init__(self):
            self.isWord = False
            self.children = [None] * 26

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie.TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for c in word:
            index = ord(c)-ord('a')
            if not p.children[index]:
                p.children[index] = Trie.TrieNode()
            p = p.children[index]
        p.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.find(word)
        return node is not None and node.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.find(prefix)
        return node is not None

    def find(self, prefix):
        p = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not p.children[index]:
                return None
            p = p.children[index]
        return p

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
