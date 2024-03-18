48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Solution:

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)

        #Logic
        #The first column of the matrix is same as that of the reverse of the first row
        #of the matrix. Hence we transpose and then reverse the matrix row wize

        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()
        
        #Alternative
        #We can make the first row as the first column in the newly created matrix but 
        #we need to allocate extra space which is the constraint given in the question.
