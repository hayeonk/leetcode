class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.d = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.d:
            return -1
        
        node = self.d[key]
        self.remove(node)
        self.insertAfter(node)
        return node.val

    def put(self, key, value):
        if key in self.d:
            self.remove(self.d[key])
        
        node = Node(key, value)
        self.d[key] = node
        self.insertAfter(node)
        
        if len(self.d) > self.capacity:
            delNode = self.tail.prev
            self.remove(delNode)
            del self.d[delNode.key]
        
    def remove(self, node):
        p = node.prev
        n = node.next
        n.prev = p
        p.next = n
        
    def insertAfter(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)