229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]

Solution:

# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         ele1=ele2=float('-inf')
#         cnt1=cnt2=0
#         for num in nums:
#             if cnt1==0 and ele2!=num:
#                 cnt1=1
#                 ele1=num
#             elif cnt2==0 and ele1!=num:
#                 cnt2=1
#                 ele2=num
#             elif num==ele1:
#                 cnt1+=1
#             elif num==ele2:
#                 cnt2+=1
#             else:
#                 cnt1-=1
#                 cnt2-=1
#         ans=[]
#         n=len(nums)
#         cnt1=cnt2=0
#         for num in nums:
#             if num==ele1:
#                 cnt1+=1
#             elif num==ele2:
#                 cnt2+=1
#         if cnt1>n/3:
#             ans.append(ele1)
#         if cnt2>n/3:
#             ans.append(ele2)
#         return ans


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1=ele2=float('-inf')
        cnt1=cnt2=0
        for num in nums:
            if cnt1==0 and ele2!=num:
                cnt1=1
                ele1=num
            elif cnt2==0 and ele1!=num:
                cnt2=1
                ele2=num
            elif num==ele1:
                cnt1+=1
            elif num==ele2:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        ans=[]
        n=len(nums)
        if nums.count(ele1)>n/3:
            ans.append(ele1)
        if nums.count(ele2)>n/3:
            ans.append(ele2)
        return ans

        
        
