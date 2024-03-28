160. Intersection of Two Linked Lists

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        addresses=set()
        while headA or headB:
            if headA:
                if headA in addresses:
                    return headA
                else:
                    addresses.add(headA)
                headA=headA.next
            if headB:
                if headB in addresses:
                    return headB
                else:
                    addresses.add(headB)
                headB=headB.next
        return
