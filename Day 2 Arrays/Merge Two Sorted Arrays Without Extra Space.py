https://www.codingninjas.com/studio/problems/merge-two-sorted-arrays-without-extra-space_6898839?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse&leftPanelTabValue=PROBLEM

'''
Given two non-decreasing sorted arrays, ‘A’ and ‘B’, having ‘N’ and ‘M’ elements, respectively.

You must merge these arrays, ‘A’ and ‘B’, into a sorted array without using extra space.
Of all the 'N + M' sorted elements, array 'A' should contain the first 'N' elements, and array 'B' should have the last 'M' elements.
'''
Solution:

from typing import *

def mergeTwoSortedArraysWithoutExtraSpace(a : List[int], b : List[int]) -> int:
    # Write your code here
    n=len(a)
    m=len(b)
    left=n-1
    right=0

    while left>=0 and right <m:
        if a[left]>b[right]:
            a[left],b[right]=b[right],a[left]
            left-=1
            right+=1
        else:
            break
    a.sort()
    b.sort()
