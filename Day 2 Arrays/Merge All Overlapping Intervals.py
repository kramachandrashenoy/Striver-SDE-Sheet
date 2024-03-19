https://www.codingninjas.com/studio/problems/merge-all-overlapping-intervals_6783452?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse&leftPanelTabValue=PROBLEM

Problem statement
Ninja is playing with intervals. He has an array of intervals called ‘Arr’ having ‘N’ intervals.
However, he doesn’t like overlapping intervals. So you must help Ninja by merging all the overlapping intervals in ‘Arr’ and return 
an array of non-overlapping intervals.

Note:
Two intervals [L1, R1] and [L2, R2] such that L1 <= L2, are said to be overlapping if and only if L2 <= R1.

Solution:

from typing import *

def mergeOverlappingIntervals(arr : List[List[int]]) -> List[List[int]]:
    # Write your code here.
    arr.sort(key=lambda x:x[0])
    ans=[]
    ans.append(arr[0])
    for i in range(1,len(arr)):
        if ans[-1][1]>=arr[i][0]:
            ans[-1][1]=max(ans[-1][1],arr[i][1])
        else:
            ans.append(arr[i])
    return ans
    
