#  https://www.codingninjas.com/studio/problems/total-unique-paths_1081470?source=youtube&campaign=striver_dp_videos&leftPanelTabValue=PROBLEM
from os import environ
from sys import *
from collections import *
from math import *

def uniquePaths(m, n):
	# Write your code here.
	dp= [[-1]*n for _ in range(m)]

	for i in range(m):
		for j in range(n):
			if i == 0 and j == 0:
				dp[0][0] = 1
			else: 
				up =0
				left =0
				if i>0:
					up = dp[i-1][j] 
				if j>0:
					left = dp[i][j-1]
				dp[i][j] = up + left

	return dp[m-1][n-1]

#### space optimized##

from os import environ
from sys import *
from collections import *
from math import *

def uniquePaths(m, n):
    # Write your code here.

    prev_row = [0] * n
    for i in range(m):
        curr_row = [0] * n
        for j in range(n):
            if i == 0 and j == 0:
                curr_row[j] = 1
            else:
                curr_row[j] = prev_row[j]
                if j >= 1:
                    curr_row[j] += curr_row[j-1]

        prev_row = curr_row
    
    return curr_row[n-1]
