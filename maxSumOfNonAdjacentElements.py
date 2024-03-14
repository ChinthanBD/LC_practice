# https://www.codingninjas.com/studio/problems/maximum-sum-of-non-adjacent-elements_843261?source=youtube&campaign=striver_dp_videos&leftPanelTabValue=PROBLEM
from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

###########################TLE for below approach###################
def maximumNonAdjacentSum(nums):    
    # Write your code here.
	def get_max_sum(n):
		if n == 0:
			return nums[n]
		if n<0:
			return 0
			
		pick = nums[n] + get_max_sum(n-2)
		non_pick = 0 + get_max_sum(n-1)
		
		return max(pick, non_pick)
		
	return get_max_sum(n-1)


###########################memoization solutionbelow#######


def maximumNonAdjacentSum(nums):    
    # Write your code here.
	dp = [-1] * len(nums)
	
	def get_max_sum(n):
		if n == 0:
			return nums[n]
		if n<0:
			return 0
		if dp[n]!=-1:
			return dp[n]
			
		pick = nums[n] + get_max_sum(n-2)
		non_pick = 0 + get_max_sum(n-1)
		dp[n] = max(pick, non_pick)
		return dp[n]
		
	return get_max_sum(n-1)
	
########################tabulation############
def maximumNonAdjacentSum(nums):    

	dp = [-1] * len(nums)
	dp[0] = nums[0]
	
	
	for i in range(1,len(nums)):
		pick = nums[i] 
		if i-2>=0:
			pick+=dp[i-2]
		
		non_pick = dp[i-1]
		
		dp[i] = max(pick, non_pick)
		
	return dp[n-1]


############Space optimization#############
def maximumNonAdjacentSum(nums):    

	prev2 = 0
	prev = nums[0]
	curri =0
	for i in range(1,len(nums)):
		pick = nums[i] + prev2
		
		non_pick = prev
		
		curri = max(pick, non_pick)
		
		prev2 = prev
		prev = curri
			
	return prev
	
	

		
# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1
