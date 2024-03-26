206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Solution:

Recursive Approach:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def func(head):
            if head is None:
                return head
            if head.next is None:
                return head
            new=func(head.next)
            head.next.next=head
            head.next=None
            return new
        return func(head)

Iterative Approach:

# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        current=head
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        return prev

