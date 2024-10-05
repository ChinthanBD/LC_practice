# https://leetcode.com/problems/climbing-stairs/description/
# pre-compute
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1) # initialize dp array to store the values at each stairs
        dp[0] = dp[1] = 1

        # Calculate the number of distinct ways for each step using dynamic programming
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]