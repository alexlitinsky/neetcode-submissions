class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class ListNode:
    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node
    
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node



class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.cap = capacity
        self.links = ListNode()
        

    def get(self, key: int) -> int:
        if key in self.lru:
            node = self.lru[key]
            self.links.remove(node)
            self.links.insert(node)
            return node.val

        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            node = self.lru[key]
            self.links.remove(node)
            del self.lru[key]
            
        new_node = Node(key, value)
        self.lru[key] = new_node
        self.links.insert(new_node)
        if len(self.lru.keys()) > self.cap:
            lru_node = self.links.left.next
            self.links.remove(lru_node)
            del self.lru[lru_node.key]
        
        
