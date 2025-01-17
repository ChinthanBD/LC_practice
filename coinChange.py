# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}  # base case: 0 coins are needed to make amount 0
        for target in range(1, amount + 1):
            dp[target] = float('inf')  # initialize with a large number
            for coin_val in coins:
                if coin_val <= target:
                    dp[target] = min(dp[target], 1 + dp[target - coin_val])

        return dp[amount] if dp[amount] != float('inf') else -1
