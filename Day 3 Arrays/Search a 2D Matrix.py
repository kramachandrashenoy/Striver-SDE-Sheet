74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Solution:

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        low=0
        high=m*n-1

        while low<=high:
            mid=(low+high)//2
            row=int(mid//n)
            col=int(mid%n)
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                high=mid-1
            else:
                low=mid+1
        return False
 

