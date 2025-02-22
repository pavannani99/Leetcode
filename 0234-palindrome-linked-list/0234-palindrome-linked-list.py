# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        hey = [] 
        while head:
            hey.append(head.val)
            head = head.next
        head1 = hey[::-1]  

    
        if hey == head1:
            return True
        return False
