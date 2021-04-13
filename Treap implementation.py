# Treap: a randomized BST
import random
import time
import os


class TreapNode():
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return '<node key:%s priority:%d left:%s right:%s>' % (self.key, self.priority,
                                                               self.left, self.right)


class Treap():
    def __init__(self):
        self.root = None

    def __repr__(self):
        return str(self.root)
    """
    Function to left-rotate a given treap
       n                    R
      / \    Left Rotate   / \
     L   R   -----------> n   Y
        / \              / \
       X   Y            L   X
    BST Feature, left: L < n < X < R < Y; right: L < n < X < R < Y, the same.
    """

    def rotateLeft(self, node):
        R = node.right
        X = node.right.left

        # rotate
        R.left = node
        node.right = X

        return R  # new root
    """
    Function to right-rotate a given treap
       n                    L
      / \    right Rotate  / \
     L   R   -----------> X   n
    / \                      / \
   X   Y                    Y   R
    BST Feature, left: X < L < Y < n < R; right: X < L < Y < n < R, the same.
    """

    def rotateRight(self, node):
        L = node.left
        Y = node.left.right

        # rotate
        L.right = node
        node.left = Y

        return L

    def _insert(self, node, newNode):
        if not node:
            node = TreapNode(newNode.key, newNode.priority)
            return node
        if newNode.key < node.key:
            node.left = self._insert(node.left, newNode)

            if node.left and node.left.priority > node.priority:
                node = self.rotateRight(node)

        else:
            node.right = self._insert(node.right, newNode)
            if node.right and node.right.priority > node.priority:
                node = self.rotateLeft(node)

        return node

    # task 1: write a TreapInsert func with two inputs (root pointer and newNode)
    # return the new root pointer of the treap
    def TreapInsert(self, newNode):
        self.root = self._insert(self.root, newNode)
        return self.root

    def _search(self, node, key):
        if not node:
            return False

        elif node.key == key:
            return True

        elif node.key > key:
            return self._search(node.left, key)

        else:
            return self._search(node.right, key)

    # task 2: write a TreapSearch func with two inputs (root pointer, key)
    # return an indication whether the key is found
    def TreapSearch(self, key):
        return self._search(self.root, key)

    def __repr__(self):
        lines = []
        nodes = [(self.root, 0)]
        while nodes:
            node, indent = nodes.pop()
            name = str(node) if node else 'None'
            lines.append(' ' * indent + name)
            if node:
                nodes.append((node.right, indent + 1))
                nodes.append((node.left, indent + 1))
                return os.linesep.join(lines)

    # task 3: use TreapInsert to build treap using uppercase letters
    # and randomly generated treap priorities for each leeter.
    def buildTreapRandom3(self, keys):
        for key in keys:
            priority = random.randrange(100)
            node = TreapNode(key, priority)
            root = self.TreapInsert(node)
            # print(root.key, root.priority)

        # print(repr(root))
        return root

    # task 5: use TreapInsert to build treap using uppercase letters
    # and fixed treap priorities correspond to average frequency of each leeter.
    def buildTreapFixed5(self, keyPri):
        for key, priority in keyPri.items():
            node = TreapNode(key, priority)
            root = self.TreapInsert(node)
            # print(root.key, root.priority)

        print(repr(root))
        return root

    # task 6: use TreapInsert to build binary search tree using uppercase letters
    # and assigning same priorities to each leeter.
    def buildTreapSame6(self, keys):
        priority = 0
        for key in keys:
            node = TreapNode(key, priority)
            root = self.TreapInsert(node)

        return root

    # task 4: wirte a func to calculate the execution time of TreapSearch.
    def searchingTime(self, treap):
        letters = []
        with open('textbook.txt', 'r', encoding='utf-8') as f:
            for lines in f.readlines():
                for c in lines:
                    if c.isalpha():
                        letters.append(c.upper())

        durations = []
        for _ in range(5):
            startTime = time.time()
            for letter in letters:
                self.TreapSearch(letter)
            endTime = time.time()
            durations.append(endTime - startTime)
        avgDuration = sum(durations) / 5.0
        return durations, avgDuration


def main():
    # treap object for task 3
    treap1 = Treap()
    keys = ['Z', 'Y', 'X', 'W', 'V', 'Q', 'U', 'P', 'S', 'R', 'K', 'J', 'G',
            'B', 'F', 'C', 'M', 'D', 'H', 'I', 'L', 'A', 'N', 'O', 'T', 'E']

    treapRanPri = treap1.buildTreapRandom3(keys)
    print("--------------------------------------------------------------")
    durationsRanPri, avgDurationRanPri = treap1.searchingTime(treapRanPri)
    print("Duration of searching with treap (random priority): " +
          str(durationsRanPri))
    print("Average duration of searching with treap (random priority): " +
          str(avgDurationRanPri))

    # treap object for task 5
    treap2 = Treap()
    keyPri = {'Z': 1, 'Y': 9, 'X': 3, 'W': 11, 'V': 6, 'Q': 2, 'U': 15,
              'P': 12, 'S': 21, 'R': 20, 'K': 5, 'J': 4, 'G': 8, 'B': 7, 'F': 10,
              'C': 14, 'M': 13, 'D': 17, 'H': 18, 'I': 22, 'L': 16, 'A': 24, 'N': 19,
              'O': 23, 'T': 25, 'E': 26}
    print("--------------------------------------------------------------")
    treapFixPri = treap2.buildTreapFixed5(keyPri)
    print("--------------------------------------------------------------")
    durationsFixPri, avgDurationFixPri = treap2.searchingTime(treapFixPri)
    print("Duration of searching with treap (fixed priority): " +
          str(durationsFixPri))
    print("Average duration of searching with treap (fixed priority): " +
          str(avgDurationFixPri))

    # treap object for task 6
    treap3 = Treap()
    keys = ['Z', 'Y', 'X', 'W', 'V', 'Q', 'U', 'P', 'S', 'R', 'K', 'J', 'G',
            'B', 'F', 'C', 'M', 'D', 'H', 'I', 'L', 'A', 'N', 'O', 'T', 'E']

    treapSamePri = treap3.buildTreapSame6(keys)
    print("--------------------------------------------------------------")
    durationsSamePri, avgDurationSamePri = treap3.searchingTime(treapSamePri)
    print("Duration of searching with binary search tree (same priority): " +
          str(durationsSamePri))
    print("Average duration of searching with binary search tree (same priority): " +
          str(avgDurationSamePri))


if __name__ == '__main__':
    main()
