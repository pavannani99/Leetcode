# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        hey = []
        while head:
            hey.append(head.val)
            head = head.next

        if not hey:
            return None

        hey = hey[::-1]

        new_head = ListNode(hey[0])
        current = new_head
        for val in hey[1:]:
            current.next = ListNode(val)
            current = current.next

        return new_head
