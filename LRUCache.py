# https://leetcode.com/problems/lru-cache/
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        ## LL to store LRU
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left 

    def insert(self, node):
        # prev, nxt = self.right.prev, self.right
        # prev.next, nxt.prev = node, node
        # node.prev, node.next = prev, nxt

        prev, nxt = self.right.prev, self.right
        prev.next, node.prev = node, prev
        node.next, nxt.prev = nxt, node


    def remove(self, node):
        if not node:
            return
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key]) 
            return self.cache[key].value
        return -1
               

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)