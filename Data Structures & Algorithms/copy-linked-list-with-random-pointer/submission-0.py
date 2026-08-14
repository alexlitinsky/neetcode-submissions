"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        deepCopy = {None : None}
        dummy = Node(0)
        curr = head
        while curr:
            copy = Node(curr.val)
            deepCopy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            node = deepCopy[curr]
            node.next = deepCopy[curr.next]
            node.random = deepCopy[curr.random]
            curr = curr.next


        return deepCopy[head]
        