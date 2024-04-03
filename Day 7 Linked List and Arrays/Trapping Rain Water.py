42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Solution:

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         left=0
#         right=len(height)-1
#         leftMax=0
#         rightMax=0
#         bucket=0
#         while left<right:
#             if height[left]<height[right]:
#                 if leftMax<height[left]:
#                     leftMax=height[left]
#                 else:
#                     bucket+=leftMax-height[left]
#                 left+=1
#             else:
#                 if rightMax<height[right]:
#                     rightMax=height[right]
#                 else:
#                     bucket+=rightMax-height[right]
#                 right-=1
#         return bucket

# Approach 2
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l=[0]*n
        r=[0]*n
        ans=0
        lm=0
        rm=0

        for i in range(n):
            l[i]=lm
            if lm<height[i]:
                lm=height[i]

        for i in range(n-1,-1,-1):
            r[i]=rm
            if rm<height[i]:
                rm=height[i]
        
        for i in range(n):
            trapped=min(l[i],r[i])-height[i]
            if trapped>0:
                ans+=trapped
        return ans


        
