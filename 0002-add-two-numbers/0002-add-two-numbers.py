# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reminder = 0
        dummy_head = ListNode(0)
        current = dummy_head

        while l1 or l2 or reminder:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + reminder
            reminder = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next

            
            