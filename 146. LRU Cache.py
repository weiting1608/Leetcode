
# Approach 1: write a double linked list (for order) + dictionary (for get and put)
# The element in dictionary is {key: node}, this way you can use key to find node and change node accordingly.
# Four func: _add_node, _remove_node, _move_to_head, pop_tail is needed as auxilary func.
# why double linked list? convinient to delete from the tail and store in the head.
# Need dummy head and tail to facilitate

class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.val = 0
        self.prev = None
        self.next = None

class LRUCache():
    def _add_node(self, node):
        """
        Always add the new node right after head
        Adding must have a reference node, like here self.head
        """
        # pay attention to the order, since self.head.next (this node) has no direct pointer, 
        # thus you need to pay attention not losing the mem location of this node.
        # Or you can do with assign a node first to take the location.
        # nex = self.head.next
        # self.head.next = node
        # node.next = nex    
        # nex.prev = node
        # node.prev = self.head
        
        node.prev = self.head # node point back to head
        node.next = self.head.next # node point to head.next
        
        self.head.next.prev = node # head.next point back to node
        self.head.next = node # head point to node
    
    def _remove_node(self, node):
        """
        remove an existing node from the linked list.
        """
        pre = node.prev
        nex = node.next
        
        pre.next = nex
        nex.prev = pre
        
    def _move_to_head(self, node):
        """
        move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node) # add right after dummy head, becomes true head 
        
    def _pop_tail(self):
        """
        pop the current tail
        """
        res = self.tail.prev # get the element before the dummy tail
        self._remove_node(res)
        return res
               
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key, None) # get key's value, default None
        if not node:
            return -1
        # move the accessed node to the head
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        
        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.val = value
            
            self.cache[key] = newNode
            # because it is new node, directly add it to the head is enough.
            self._add_node(newNode) 
            self.size += 1
            
            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
                
        else:
            node.val = value
            self._move_to_head(node)
               

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Approach 2: use the python built-in structure OrderedDict
# Take advantage of the function move_to_end and popitem to realize the LRU order.
from collections import OrderedDict

class LRUCache(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity
        
    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]
    
    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        
        if len(self) > self.capacity:
            self.popitem(last = False)
            
            
            