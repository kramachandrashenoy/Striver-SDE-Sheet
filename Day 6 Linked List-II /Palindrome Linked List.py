234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        prev=slow.next
        slow.next=None
        temp=None
        while prev:
            temp2=prev.next
            prev.next=temp
            temp=prev
            prev=temp2
        
        while temp and head:
            if temp.val!=head.val:
                return False
            head=head.next
            temp=temp.next
        return True
