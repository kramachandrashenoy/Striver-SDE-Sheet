19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        first=second=dummy
        for i in range(n+1):
            first=first.next
        while first:
            first=first.next
            second=second.next
        second.next=second.next.next
        return dummy.next
        
