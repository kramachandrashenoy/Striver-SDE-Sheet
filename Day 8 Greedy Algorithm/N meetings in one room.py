There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?

Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

Example 1:

Input:
N = 6
start[] = {1,3,0,5,8,5}
end[] =  {2,4,6,7,9,9}
Output: 
4
Explanation:
Maximum four meetings can be held with
given start and end timings.
The meetings are - (1, 2),(3, 4), (5,7) and (8,9)

Solution:

    def maximumMeetings(self,n,start,end):
        # code here
        new=list(zip(start,end))
        new.sort(key=lambda x:x[1])
        l=[]
        l.append(new[0])
        end=new[0][1]
        for num in new[1:]:
            if num[0]>end:
                end=num[1]
                l.append(num)
        return len(l)
