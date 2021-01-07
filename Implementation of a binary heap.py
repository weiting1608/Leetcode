
"""
Implementation of a max heap
First element starts from array[0], no dummy
"""
class MaxHeap:
    def __init__(self):
        self.heap =[]

    def get_parent(self, i):
        return (i-1)//2

    def get_leftChild(self, i):
        return 2*i+1

    def get_rightChild(self,i):
        return 2*i+2

    
    def has_parent(self,i):
        return self.get_parent(i) >= 0

    def has_leftChild(self,i):
        return self.get_leftChild(i) < len(self.heap)

    def has_rightChild(self,i):
        return self.get_rightChild(i) < len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    def insert_key(self,key):
        self.heap.append(key)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self,i):
        size = len(self.heap)
        while(self.has_parent(i) and self.heap[i] > self.heap[self.get_parent(i)]):
            self.swap(i, self.get_parent(i))
            i = self.get_parent(i)

    def print_heap(self):
        print(self.heap)

    def delete_root(self):
        if len(self.heap) == 0: return -1
        last_index = len(self.heap)-1
        self.swap(0, last_index)
        root = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_down(self,i):
        while self.has_leftChild(i):
            max_childIndex = self.get_maxChildIndex(i)
            if max_childIndex == -1: break
            if self.heap[i] < self.heap[max_childIndex]:
                self.swap(i,max_childIndex)
                i = max_childIndex
            else: break
    
    def get_maxChildIndex(self, i):
        if self.has_leftChild(i):
            leftChild = self.get_leftChild(i)
            if self.has_rightChild(i):
                rightChild = self.get_rightChild(i)
                return max(leftChild, rightChild)
        else: return -1

max_heap = MaxHeap()

# random array
array = [23,543,12,3,6,2,645,32,87,27]

# build the max heap
for ele in array:
    max_heap.insert_key(ele)

print("Initial heap")
max_heap.print_heap()
print("After insert key 100")
max_heap.insert_key(100)
max_heap.print_heap()
print("After delete root node")
max_heap.delete_root()
max_heap.print_heap()


    