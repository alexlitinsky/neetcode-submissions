# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        carry = 0

        curr = dummy

        while carry or l1 or l2:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            val = (first + second + carry) % 10
            carry = (first + second + carry) // 10
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            node = ListNode(val)
            curr.next = node
            curr = curr.next

        return dummy.next

        



        