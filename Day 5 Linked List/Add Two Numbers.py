2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=remainder=0
        total=0
        dummy=new=ListNode()
        while l1 or l2 or carry:
            total=carry
            if l1:
                total+=l1.val
                l1=l1.next
            if l2:
                total+=l2.val
                l2=l2.next
            remainder=total%10
            carry=total//10
            dummy.next=ListNode(remainder)
            dummy=dummy.next
        return new.next

Method 2:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        temp=l1
        while temp:
            s1+=str(temp.val)
            temp=temp.next
        s2=""
        temp=l2
        while temp:
            s2+=str(temp.val)
            temp=temp.next
        ans=str(int(s1[::-1])+int(s2[::-1]))
        ans=ans[::-1]
        new=temp=ListNode()
        for i in range(len(ans)):
            new.next=ListNode(ans[i])
            new=new.next
        return temp.next

        
