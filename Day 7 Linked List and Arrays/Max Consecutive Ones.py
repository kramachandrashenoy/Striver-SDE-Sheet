485. Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.


Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

Solution:
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        maxi=0
        for num in nums:
            if num==1:
                ans+=1
                maxi=max(ans,maxi)
            else:
                ans=0

        return maxi

Alternative:
 Using Sliding Window
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=j=0
        n=len(nums)
        maxi=0
        while j<n:
            if nums[j]==1:
                j+=1
            else:
                maxi=max(j-i,maxi)
                j+=1
                i=j
        return max(j-i,maxi)


