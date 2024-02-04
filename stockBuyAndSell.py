# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 999999
        max_profit = 0
        for i in range(len(prices)):
            if prices[i]< min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit