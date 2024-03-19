Problem statement
You are given an array of size ‘N’. The elements of the array are in the range from 1 to ‘N’.

Ideally, the array should contain elements from 1 to ‘N’. But due to some miscalculations, there is a number R in the range [1, N]
 which appears in the array twice and another number M in the range [1, N] which is missing from the array.

Your task is to find the missing number (M) and the repeating number (R).

For example:
Consider an array of size six. The elements of the array are { 6, 4, 3, 5, 5, 1 }. 
The array should contain elements from one to six. Here, 2 is not present and 5 is occurring twice. Thus, 2 is the missing number (M) 
and 5 is the repeating number (R). 
Follow Up
Can you do this in linear time and constant additional space? 

Solution:

from math import *
from collections import *
from sys import *
from os import *

def missingAndRepeating(arr, n):
    # Write your code here
    s=(n*(n+1))//2
    ss=(n*(n+1)*(2*n+1))//6

    summ=0
    summsq=0
    for num in arr:
        summ+=num
        summsq+=num*num


    #Logic
    #Let Missing number be x and repeating number be y
    #s-summ=x-y
    #ss-summsq=x^2-y^2
    #x^2-y^2=(x+y)*(x-y)

    addition=(ss-summsq)//(s-summ)  #x+y

    x=(addition+s-summ)//2
    y=addition-x
    return [x,y]
    pass

