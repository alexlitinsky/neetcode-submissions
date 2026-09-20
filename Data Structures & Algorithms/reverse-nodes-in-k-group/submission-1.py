# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        prevGroup = dummy

        while True:
            kth = self.nextKth(head, k)
            if not kth: return dummy.next
            nextGroup = kth.next
            prev = nextGroup

            oldGroup = head
            while head != nextGroup:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            
            prevGroup.next = kth
            head = nextGroup 
            prevGroup = oldGroup  
            
    def nextKth(self, cur, k):
        while cur and k > 1:
            cur = cur.next
            k -= 1
        return cur

        