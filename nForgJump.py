# https://www.codingninjas.com/studio/problems/frog-jump_3621012?source=youtube&campaign=striver_dp_videos&leftPanelTabValue=PROBLEM
from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:
    dp = [None] * n
    def func(step, dp, heights):
        if step == 0:
            return 0
        if dp[step] is not None:
            return dp[step]

        left = func(step-1, dp, heights) + abs(heights[step] - heights[step-1])
        right = float("inf")

        if step > 1:
            right = func(step-2, dp, heights) + abs(heights[step] - heights[step-2])

        dp[step] = min(left, right)
        return dp[step]

    return func(n-1, dp, heights)

##########################

def frogJump(n: int, heights: List[int]) -> int:

    if n <= 1:
        return 0 

    dp = [0] * n  
    dp[1] = abs(heights[1] - heights[0])  
    for i in range(2, n):
        jump1 = dp[i-1] + abs(heights[i] - heights[i-1])  
        jump2 = dp[i-2] + abs(heights[i] - heights[i-2])  
        dp[i] = min(jump1, jump2)  
    
    return dp[n-1]

##########################
def frogJump(n: int, heights: List[int]) -> int:
    prev = 0 
    prev2 = 0
    for i in range(1,n):
        fs = prev + abs(heights[i]-heights[i-1])
        ss = float("inf")

        if i >1:
            ss = prev2 + abs(heights[i]-heights[i-2])
        
        curri = min(fs,ss)
        prev2 = prev
        prev = curri
    
    return prev