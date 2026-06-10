class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key -> node
        self.capacity = capacity

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def _remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def _insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity:
            node = self.left.next
            self._remove(node)
            del self.cache[node.key]
        
