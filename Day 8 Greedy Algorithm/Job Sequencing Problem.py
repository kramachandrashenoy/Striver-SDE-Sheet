You are given a 'Nx3' 2-D array 'Jobs' describing 'N' jobs where 'Jobs[i][0]' denotes the id of 'i-th' job, 'Jobs[i][1]' denotes the deadline of 'i-th' job, and 
'Jobs[i][2]' denotes the profit associated with 'i-th job'.
You will make a particular profit if you complete the job within the deadline associated with it. Each job takes 1 unit of time to be completed, 
and you can schedule only one job at a particular time.
Return the number of jobs to be done to get maximum profit.

For Example :
'N' = 3, Jobs = [[1, 1, 30], [2, 3, 40], [3, 2, 10]].

All the jobs have different deadlines. So we can complete all the jobs.

At time 0-1, Job 1 will complete.
At time 1-2, Job 3 will complete.
At time 2-3, Job 2 will complete.

So our answer is [3 80].

Solution:

def jobScheduling(jobs):

    # Write your code here
    # Return an integer denoting the maximum pofit  
    jobs.sort(key=lambda x: (x[1], -x[2]))

    minHeap = []
    for _, deadline, profit in jobs:
        heapq.heappush(minHeap, profit)
        if len(minHeap) >= deadline+1:
            heapq.heappop(minHeap)
    
    return [len(minHeap), sum(minHeap)]


