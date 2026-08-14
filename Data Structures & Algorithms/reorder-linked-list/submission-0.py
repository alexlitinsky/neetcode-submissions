# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        dummy = ListNode(head)

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next
        

        # we go to the next one so its easier?
        second, prev = slow.next, None

        # we have to split the lists
        slow.next = None

        while second:
            nxt = second.next 
            second.next  = prev 
            prev = second
            second = nxt
        
        second = prev
        first = head

        # save copies to remove cyclical nature
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            first = t1
            second.next = first
            second = t2
        
        return dummy.next

        