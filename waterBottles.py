# https://leetcode.com/problems/water-bottles/description/?envType=daily-question&envId=2024-07-07
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_bottles = numBottles  # Start with the initial number of bottles
        empty_bottles = numBottles  # Initial empty bottles are the same as the initial full bottles
        
        while empty_bottles >= numExchange:
            new_bottles = empty_bottles // numExchange  # Calculate new full bottles from exchanges
            total_bottles += new_bottles  # Add the new full bottles to the total count
            empty_bottles = empty_bottles % numExchange + new_bottles  # Update empty bottles
            
        return total_bottles