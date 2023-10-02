# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        lenA = self.getLength(headA)
        lenB = self.getLength(headB)


        if lenA > lenB:
            for _ in range(lenA - lenB):
                headA = headA.next
        elif lenB > lenA:
            for _ in range(lenB - lenA):
                headB = headB.next


        while headA is not None and headB is not None:
            if headA == headB:
                return headA 
            headA = headA.next
            headB = headB.next

        return None 

    def getLength(self, head: ListNode) -> int:
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length
