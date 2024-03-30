Flattening a Linked List

Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 

Note: The flattened list will be printed using the bottom pointer instead of the next pointer.
For more clarity have a look at the printList() function in the driver code.

Solution:

def flatten(root):
    #Your code here
    cur=root
    l=[]
    
    while cur!=None:
        temp=cur
        while temp!=None:
            l.append(temp.data)
            temp=temp.bottom
        cur=cur.next
    
    l.sort()
    dummy=cur=Node(l[0])
    for num in l[1:]:
        dummy.bottom=Node(num)
        dummy=dummy.bottom

    
    return cur
